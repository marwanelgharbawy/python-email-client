import imaplib
import email
import os
from email.header import decode_header
from dotenv import load_dotenv

load_dotenv()

def fetch_latest_email(email, password):
    try:   
        # connect to IMAP server and login
        # modify the server address depending on the recepient (ex: imap.yahoo.com)
        con = imaplib.IMAP4_SSL("imap.gmail.com")
        con.login(email, password)
        con.select("Inbox")
        
        print("Connected successfully to the email server.")
        
        
        
        return True

    except imaplib.IMAP4.error as e:
        print(f"IMAP Error: Authentication failed or server issue. {e}")
        return False
    except Exception as e:
        print(f"An error occurred while connecting: {e}")
        return False

if __name__ == "__main__":
    load_dotenv()
    # test
    email_address = os.getenv("EMAIL_ADDRESS")
    email_password = os.getenv("EMAIL_PASSWORD")
    
    if fetch_latest_email(email_address, email_password):
        print("Email fetching process completed.")
    else:
        print("Failed to fetch emails.")