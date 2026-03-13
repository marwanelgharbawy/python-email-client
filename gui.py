import tkinter as tk
from tkinter import messagebox
from send_email import send_email
from receive_email import fetch_latest_email

def login():
    global user_email, user_password
    if email_entry.get() and password_entry.get():
        user_email = email_entry.get()
        user_password = password_entry.get()
        
        # Hide login window and open main dashboard
        login_window.withdraw()
        open_main_window()
    else:
        messagebox.showwarning("Missing Information", "Please enter your email and password.")

def send():
    if email_entry.get() and password_entry.get() and recipient_entry.get() and body_text.get("1.0", tk.END).strip():
        
        sender_email = email_entry.get()
        sender_password = password_entry.get()
        recipient_email = recipient_entry.get()
        subject = subject_entry.get() if subject_entry.get() else "No Subject"
        body = body_text.get("1.0", tk.END).strip()
        
        if send_email(sender_email, sender_password, recipient_email, subject, body):
            messagebox.showinfo("Success", "Email sent successfully.")
        else:
            messagebox.showerror("Error", "Failed to send email. Please check your credentials and try again.")
    else:
        messagebox.showwarning("Missing Information", "Please fill all required fields.")

def receive():
    if email_entry.get() and password_entry.get():
        latest_email = fetch_latest_email(email_entry.get(), password_entry.get())
        if latest_email:
            messagebox.showinfo("Latest Email", f"From: {latest_email['from']}\n\nSubject: {latest_email['subject']}\n\n{latest_email['body']}")
        else:
            messagebox.showerror("Error", "Failed to fetch latest email.")
    else:
        messagebox.showwarning("Missing Information", "Please enter your email and password to receive emails.")

def open_main_window():
    global recipient_entry, subject_entry, body_text
    
    main_window = tk.Toplevel() # seconday window for email functionality
    main_window.title("Welcome!")
    main_window.geometry("400x500")
    
    # close the entire app when secondary window is closed
    main_window.protocol("WM_DELETE_WINDOW", login_window.destroy)

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