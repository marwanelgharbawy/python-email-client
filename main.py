import tkinter as tk
from tkinter import messagebox
from send_email import send_email
from receive_email import fetch_latest_email, get_connection
from plyer import notification
import threading
import time

user_email = None
user_password = None
latest_email = None
con = None

def login():
    global user_email, user_password, latest_email, con
    
    email = email_entry.get()
    password = password_entry.get()       
        
    if email and password:
        # attempt connection and login
        con = get_connection(email, password)
        
        if con:
            user_email = email
            user_password = password
            latest_email = fetch_latest_email(con)
            
            login_window.withdraw()
            open_main_window()
        else:
            messagebox.showerror("Login Failed", "Could not connect to server. Check credentials or IMAP settings.")
    else:
        messagebox.showwarning("Missing Information", "Please enter your email and password.")

def send():
    if recipient_entry.get() and body_text.get("1.0", tk.END).strip():
        # form data
        recipient_email = recipient_entry.get()
        subject = subject_entry.get() if subject_entry.get() else "No Subject"
        body = body_text.get("1.0", tk.END).strip()
        
        if send_email(user_email, user_password, recipient_email, subject, body):
            messagebox.showinfo("Success", "Email sent successfully.")
        else:
            messagebox.showerror("Connection Error", "Failed to send email.")
    else:
        messagebox.showwarning("Missing Information", "Please fill all required fields.")

def receive():
    global latest_email
    fetched_email = fetch_latest_email(con)
    if fetched_email:
        latest_email = fetched_email
        messagebox.showinfo("Latest Email", f"From: {latest_email['from']}\n\nSubject: {latest_email['subject']}\n\n{latest_email['body']}")
    else:
        messagebox.showerror("Error", "Failed to fetch latest email.")
        
# def poll_emails(window):
#     global latest_email
    
#     current_email = fetch_latest_email(con)
#     print("Checking for new emails NOW.")
    
#     # check if a new email arrived by comparing with the stored one
#     if current_email and current_email != latest_email:
#         latest_email = current_email
        
#         print("Notifying!")
        
#         notification.notify(
#             title=f"New Email: {latest_email['subject']}",
#             message=f"From: {latest_email['from']}",
#             app_name="Email Client",
#             timeout=10
#         )
        
#     # schedule this function to run again periodically
#     window.after(10000, lambda: poll_emails(window))

def open_main_window():
    global recipient_entry, subject_entry, body_text
    
    main_window = tk.Toplevel() # seconday window for email functionality
    main_window.title("Welcome!")
    main_window.geometry("400x500")
    
    # close the entire app when secondary window is closed
    main_window.protocol("WM_DELETE_WINDOW", on_closing)

    # email sending form
    tk.Label(main_window, text="Recipient Email:").pack(pady=(10, 2), padx=10, anchor="w")
    recipient_entry = tk.Entry(main_window, width=40)
    recipient_entry.pack(pady=2, padx=10, anchor="w")

    tk.Label(main_window, text="Subject:").pack(pady=2, padx=10, anchor="w")
    subject_entry = tk.Entry(main_window, width=40)
    subject_entry.pack(pady=2, padx=10, anchor="w")

    tk.Label(main_window, text="Body:").pack(pady=2, padx=10, anchor="w")
    body_text = tk.Text(main_window, width=45, height=15)
    body_text.pack(pady=2, padx=10, anchor="w")

    send_button = tk.Button(main_window, text="Send Email", command=send)
    send_button.pack(pady=5, padx=10, anchor="w")

    receive_button = tk.Button(main_window, text="Receive Latest Email", command=receive)
    receive_button.pack(pady=5, padx=10, anchor="w")
    
    start_polling_thread()

def on_closing():
    global con
    if con:
        try:
            con.logout()
        except:
            pass
    login_window.destroy()
    
def start_polling_thread():
    thread = threading.Thread(target=background_poll, daemon=True) # ensures the thread dies when the main program closes
    thread.start()

def background_poll():
    global latest_email, con
    while True:
        print("Checking for new emails NOW.")
        if con:
            try:
                current_email = fetch_latest_email(con)
                
                if current_email and current_email != latest_email:
                    latest_email = current_email
                    
                    print("Notifying!")
                    
                    notification.notify(
                        title=f"New Email: {latest_email['subject']}",
                        message=f"From: {latest_email['from']}",
                        app_name="Email Client",
                        timeout=10
                    )
            except Exception as e:
                print(f"Polling error: {e}")
        
        # wait 10 seconds before checking again
        time.sleep(10)

# login window
login_window = tk.Tk() # first window to start with
login_window.title("Login")
login_window.geometry("300x200")

tk.Label(login_window, text="Email:").pack(pady=(20, 2), padx=10, anchor="w")
email_entry = tk.Entry(login_window, width=35)
email_entry.pack(pady=2, padx=10, anchor="w")

tk.Label(login_window, text="Password:").pack(pady=2, padx=10, anchor="w")
password_entry = tk.Entry(login_window, width=35, show="*")
password_entry.pack(pady=2, padx=10, anchor="w")

login_button = tk.Button(login_window, text="Login", command=login)
login_button.pack(pady=15, padx=10, anchor="w")

login_window.mainloop()