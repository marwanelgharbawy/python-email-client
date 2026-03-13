import tkinter as tk
from tkinter import messagebox
from send_email import send_email
from receive_email import fetch_latest_email

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

# Main window setup
root = tk.Tk()
root.title("Email Client")
root.geometry("400x500")

# input fields
# email and password
tk.Label(root, text="Your Email:").pack(pady=2)
email_entry = tk.Entry(root, width=40)
email_entry.pack(pady=2)

tk.Label(root, text="Password:").pack(pady=2)
password_entry = tk.Entry(root, width=40, show="*")
password_entry.pack(pady=2)

# email details
tk.Label(root, text="Recipient Email:").pack(pady=2)
recipient_entry = tk.Entry(root, width=40)
recipient_entry.pack(pady=2)

tk.Label(root, text="Subject:").pack(pady=2)
subject_entry = tk.Entry(root, width=40)
subject_entry.pack(pady=2)

tk.Label(root, text="Body:").pack(pady=2)
body_text = tk.Text(root, width=40, height=10)
body_text.pack(pady=2)

# buttons
send_button = tk.Button(root, text="Send Email", command=send)
send_button.pack(pady=5)

receive_button = tk.Button(root, text="Receive Latest Email", command=receive)
receive_button.pack(pady=5)

root.mainloop()