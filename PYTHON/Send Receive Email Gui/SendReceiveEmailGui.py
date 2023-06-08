# GUI & Email Library
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import smtplib
import imaplib
from email.message import EmailMessage

def send_email():
    # Mengambil informasi dari input pengguna
    sender_email = sender_email_entry.get()
    sender_password = sender_password_entry.get()
    recipient_email = recipient_email_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", "end-1c")

    try:
        # Mengatur koneksi ke server SMTP
        smtp_server = "smtp.gmail.com"  # Ubah dengan server SMTP yang sesuai
        smtp_port = 587  # Ubah dengan port yang sesuai
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.starttls()

        # Login ke akun pengirim
        smtp_connection.login(sender_email, sender_password)

        # Membuat email
        email = EmailMessage()
        email["From"] = sender_email
        email["To"] = recipient_email
        email["Subject"] = subject
        email.set_content(message)

        # Mengirim email
        smtp_connection.send_message(email)
        smtp_connection.quit()

        messagebox.showinfo("Success", "Email has been sent successfully!")
    except smtplib.SMTPAuthenticationError:
        messagebox.showerror("Error", "Failed to authenticate. Please check your email and password.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def receive_email():
    # Mengambil informasi dari input pengguna
    recipient_email = recipient_email_entry.get()
    recipient_password = recipient_password_entry.get()

    try:
        # Mengatur koneksi ke server IMAP
        imap_server = "imap.gmail.com"  # Ubah dengan server IMAP yang sesuai
        imap_port = 993  # Ubah dengan port yang sesuai
        imap_connection = imaplib.IMAP4_SSL(imap_server, imap_port)

        # Login ke akun penerima
        imap_connection.login(recipient_email, recipient_password)
        imap_connection.select("INBOX")

        # Mencari email yang belum dibaca
        _, data = imap_connection.search(None, "UNSEEN")
        email_ids = data[0].split()

        if len(email_ids) == 0:
            messagebox.showinfo("No New Emails", "There are no new emails.")
        else:
            messagebox.showinfo("New Emails", f"There are {len(email_ids)} new email(s).")

        # Menampilkan detail email
        for email_id in email_ids:
            _, email_data = imap_connection.fetch(email_id, "(RFC822)")
            raw_email = email_data[0][1]
            email_message = EmailMessage()
            email_message.parse_bytes(raw_email)

            messagebox.showinfo("Email Details",
                                f"From: {email_message['From']}\n"
                                f"To: {email_message['To']}\n"
                                f"Subject: {email_message['Subject']}\n"
                                f"\n{email_message.get_content()}")

        imap_connection.logout()
    except imaplib.IMAP4.error as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Membuat GUI
window = Tk()
window.title("Send and Receive Email")

# Frame Utama Untuk Label & Entry
window.geometry("430x420")
window.resizable(False, False)

# Membuat style untuk entry dengan radius
style = ttk.Style()
style.configure("RoundedEntry.TEntry", borderwidth=0, relief="solid", 
                padding=5, bordercolor="#bfbfbf", 
                background="#ffffff", foreground="#000000", 
                focuscolor="#80bdff", fieldbackground="#ffffff")

# Jenis Font
font_style = ("Arial", 9)

# Label & Entry Untuk Sender Email
sender_email_label = Label(window, text = "Sender Email : ", anchor = "e")
sender_email_label.grid(row = 0, column = 0, sticky = "E")
sender_email_entry = ttk.Entry(window, width = 30, justify = CENTER, style="RoundedEntry.TEntry", font = font_style)
sender_email_entry.grid(row = 0, column = 1, pady = 10)

# Label & Entry Untuk Password
sender_password_label = Label(window, text = "Sender Password : ", anchor = "e")
sender_password_label.grid(row = 1, column = 0, sticky = "E")
sender_password_entry = ttk.Entry(window, width = 30, justify = CENTER, show = "*", style="RoundedEntry.TEntry", font = font_style)
sender_password_entry.grid(row = 1, column = 1, pady = 5)

# Label & Entry Untuk Recipient Email
recipient_email_label = Label(window, text = "Recipient Email : ")
recipient_email_label.grid(row = 2, column = 0, sticky = "E")
recipient_email_entry = ttk.Entry(window, width = 30, justify = CENTER, style="RoundedEntry.TEntry", font = font_style)
recipient_email_entry.grid(row = 2, column = 1, pady = 5)

# Label & Entry Untuk Recipient Password
recipient_password_label = Label(window, text = "Recipient Password : ", anchor = "e")
recipient_password_label.grid(row = 3, column = 0, sticky = "E")
recipient_password_entry = ttk.Entry(window, width = 30, justify = CENTER, show = "*", style="RoundedEntry.TEntry", font = font_style)
recipient_password_entry.grid(row = 3, column = 1, pady = 5)

# Label & Entry Untuk Subject
subject_label = Label(window, text = "Subject : ")
subject_label.grid(row = 4, column = 0, sticky = "E")
subject_entry = ttk.Entry(window, width = 30, justify = CENTER, style="RoundedEntry.TEntry", font = font_style)
subject_entry.grid(row = 4, column = 1, pady = 5)

# # Label & Text Untuk Message
message_label = Label(window, text = "Message : ")
message_label.grid(row = 5, column = 0, sticky = "NE")
message_text = Text(window, height = 10, width = 40, font = font_style)
message_text.grid(row = 5, column = 1, padx = 10, pady = 10)

# Tombol Kirim Email
send_button = ttk.Button(window, text = "Send Email", command = send_email)
send_button.place(x = 165, y = 380, width = 100, height = 30)

# Tombel Menerima Email
receive_button = ttk.Button(window, text = "Email Received", command = receive_email)
receive_button.place(x = 275, y = 380, width = 100, height = 30)

window.mainloop()