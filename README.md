# Email Client Application 

## Objective
This is a Python-based email client application that can send and receive emails using the smtplib and imaplib libraries. The application is able to establish a TCP connection with a mail server, dialogue with the mail server using the SMTP and IMAP protocols, send an e-mail message to a recipient via the mail server, fetch the latest email from the mailbox, and finally close the TCP connection with the mail server.

It also features threading to allow for background polling of new emails without freezing the GUI, and uses the plyer library to send desktop notifications when new emails arrive.

## Dependencies, Installation, and Running
To run this application, Python 3.x must be installed on your system. The application relies on standard Python libraries (imaplib, smtplib, email, tkinter, threading, time and external dependencies). Install missing dependencies using `pip`:
   `pip install plyer, python-dotenv`

Note: `dotenv` is only required if running the scripts on their own without GUI, as user will input the credentials in the GUI form.

**To Run the Application**
1. Ensure all Python scripts are located in the same directory.
2. Open your terminal and navigate to the project directory.
3. Execute the main GUI script:
   `python main.py`

## Usage Instructions
1. **Login:** Input the email and password in the login page. Once authenticated, a persistent server connection is established.
2. **Dashboard:** The main dashboard will open, granting access to the email functionalities.
3. **Sending an Email:** Fill in the recipient's email, subject, and body. Use the send button to send emails.
4. **Receiving Emails:** Click the button to receive emails to manually fetch the latest email from the mailbox and print its body in a dialog box.
5. **Push Notifications:** Every few seconds, if a new email is received, a push notification will be sent through the device to notify the user.
<!-- 
## Testing Process and Results
Tested the application by sending emails to different user accounts. -->

<!-- TODO: Put screenshots -->
<!-- 
* **Test Case 1: Authentication & UI Transition**
    * *Result:* The login window successfully captures credentials, establishes the persistent connection, and transitions to the main dashboard.
    * *[Insert Screenshot of Login Window here]*
* **Test Case 2: Sending an Email**
    * *Result:* The application successfully connected to the SMTP server and delivered the email with the correct subject and body.
    * *[Insert Screenshot of Success Message and Received Email here]*
* **Test Case 3: Receiving an Email & Background Thread Polling**
    * *Result:* The application successfully fetched the latest email. The background daemon thread successfully triggered a system notification when a new email arrived without freezing the GUI.
    * *[Insert Screenshot of the Plyer Desktop Notification here]*
* **Test Case 4: Error Handling**
    * *Result:* Missing fields or bad connections trigger the correct UI warnings and handle errors gracefully.
    * *[Insert Screenshot of Error Dialog here]* -->