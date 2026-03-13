import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

# function to send email, takes parameters from user
def send_email(sender_email, sender_password, recipient_email, subject, body):
    
    # create main email object
    email = MIMEMultipart()
    
    # modify headers
    email['From'] = sender_email
    email['To'] = recipient_email
    email['Subject'] = subject
    
    # add body to email
    email.attach(MIMEText(body, 'plain'))
    try:
        # create a session and connect to SMTP server
        # 587 port number is for Gmail
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender_email, sender_password)
        text = email.as_string()
        s.sendmail(sender_email, recipient_email, text)
        
        print("Email sent successfully.")
        
        s.quit()
    except smtplib.SMTPAuthenticationError as e:
        print(f"SMTP Authentication Error: {e}")
        return False
    
    return True
    
if __name__ == "__main__":
    load_dotenv()
    
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")
    recipient_email = os.getenv("RECIPIENT_ADDRESS")
    subject = "This is an email"
    body = "Good day!!\nKindly note that this is an email.\nBest regards."
    if send_email(sender_email, sender_password, recipient_email, subject, body):
        print("Email sending process completed.")
    else:
        print("Failed to send email.")