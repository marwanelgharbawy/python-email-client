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

# stay connected by returning connection object
def get_connection(email_address, password):
    try:
        con = imaplib.IMAP4_SSL("imap.gmail.com")
        con.login(email_address, password)
        con.select("Inbox")
        return con
    except Exception as e:
        print(f"Connection failed: {e}")
        return None

def fetch_latest_email(con):
    try:
        con.select("Inbox")
        status, messages = con.search(None, 'ALL')
        mail_ids = messages[0].split()
        if mail_ids:
            latest_id = mail_ids[-1]
            status, msg_data = con.fetch(latest_id, '(RFC822)')
            
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    return {
                        'from': msg['From'],
                        'subject': msg['Subject'],
                        'body': get_body(msg)
                    }
        return None
    except imaplib.IMAP4.error as e:
        print(f"IMAP Error: Authentication failed or server issue. {e}")
        return None
    except Exception as e:
        print(f"Error fetching: {e}")
        return None

if __name__ == "__main__":
    load_dotenv()
    # test
    email_address = os.getenv("RECIPIENT_ADDRESS")
    email_password = os.getenv("RECIPIENT_PASSWORD")
    
    con = get_connection(email_address, email_password)
    
    if con:
        print("Connection successful.")     
        if fetch_latest_email(con):
            print("\nEmail fetching process completed.")
        else:
            print("Failed to fetch emails.")
        