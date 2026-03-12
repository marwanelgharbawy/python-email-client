import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

    # create a session and connect to SMTP server
    # 587 port number is for Gmail
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_email, sender_password)
    text = email.as_string()
    s.sendmail(sender_email, recipient_email, text)
    s.quit()
    
if __name__ == "__main__":
    sender_email = input("Enter your email address: ")
    sender_password = input("Enter your email password: ")
    recipient_email = input("Enter recipient's email address: ")
    subject = "Testing my code"
    body = "Ramadan Mubarak!!"
    
    send_email(sender_email, sender_password, recipient_email, subject, body)