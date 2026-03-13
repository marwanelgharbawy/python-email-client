import imaplib
import email
import os
from email.header import decode_header
from re import search
from dotenv import load_dotenv

def get_body(msg):
    if msg.is_multipart():
        body = msg.get_payload(0).get_payload(decode=True).decode(errors='ignore')
    else:
        body = msg.get_payload(decode=True).decode(errors='ignore')
    return body

def fetch_latest_email(email_address, password):
    try:   
        # connect to IMAP server and login
        # modify the server address depending on the recepient (ex: imap.yahoo.com)
        con = imaplib.IMAP4_SSL("imap.gmail.com")
        con.login(email_address, password)
        con.select("Inbox")
        
        print("Connected successfully to the email server.")
        
        status, messages = con.search(None, 'ALL')
        
        # "messages" contain a list of email ids -> split to get ids
        mail_ids = messages[0].split()
        if mail_ids:
            # get last email id and fetch the email using RFC822 protocol
            latest_id = mail_ids[-1]
            status, msg_data = con.fetch(latest_id, '(RFC822)')
            
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    
                    print(f"From: {msg['From']}")
                    print(f"Subject: {msg['Subject']}")
                    print(f"Body:\n{get_body(msg)}")
                    
                    # dictionary for GUI
                    email_data = {
                        'from': msg['From'],
                        'subject': msg['Subject'],
                        'body': get_body(msg)
                    }
        else:
            print("No emails found.")
        
        con.close()
        con.logout()
        return email_data

    except imaplib.IMAP4.error as e:
        print(f"IMAP Error: Authentication failed or server issue. {e}")
        return False
    except Exception as e:
        print(f"An error occurred while connecting: {e}")
        return False

if __name__ == "__main__":
    load_dotenv()
    # test
    email_address = os.getenv("RECIPIENT_ADDRESS")
    email_password = os.getenv("RECIPIENT_PASSWORD")
    
    if fetch_latest_email(email_address, email_password):
        print("\nEmail fetching process completed.")
    else:
        print("Failed to fetch emails.")