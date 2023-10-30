# Mail Application With GUI Using Python.
import tkinter
import tkinter as tk
import smtplib

class MailApp:
    def __init__(self, master):
        self.master = master
        master.title("GMail")
        tkinter.Tk.config(master, background="sky blue")

        # Create the UI
        self.from_label = tk.Label(master, text="From:       ", background="Purple", foreground="White")
        self.from_label.grid(row=0, column=0, sticky="w", padx=6)
        self.from_entry = tk.Entry(master, width=60)
        self.from_entry.grid(row=0, column=1, sticky="w", pady=11)

        self.pass_label = tk.Label(master, text="App Password:       ", background="Purple", foreground="White")
        self.pass_label.grid(row=1, column=0, sticky="w", padx=6)
        self.pass_entry = tk.Entry(master, width=60, show="*")
        self.pass_entry.grid(row=1, column=1, sticky="w", pady=11)

        self.to_label = tk.Label(master, text="To:        ", background="Purple", foreground="White")
        self.to_label.grid(row=2, column=0, sticky="w", padx=6)
        self.to_entry = tk.Entry(master, width=6)
        self.to_entry.grid(row=2, column=1, sticky="w", pady=11)

        self.subject_label = tk.Label(master, text="Subject:     ", background="Purple", foreground="White")
        self.subject_label.grid(row=3, column=0, sticky="w", padx=5)
        self.subject_entry = tk.Entry(master, width=60)
        self.subject_entry.grid(row=3, column=1, sticky="w", pady=10)

        self.body_label = tk.Label(master, text="Body:     ", background="Purple", foreground="White")
        self.body_label.grid(row=4, column=0, sticky="w", padx=5)
        self.body_text = tk.Text(master, height=7, width=60)
        self.body_text.grid(row=4, column=1, sticky="w", pady=20)

        self.send_button = tk.Button(master, text="Send", command=self.send_mail, width=16,
                                     background="Purple", foreground="White", font=9)
        self.send_button.grid(row=5, column=0, columnspan=3, sticky="w", padx=200)

    def send_mail(self):
        # Get the email data from the UI
        from_address = self.from_entry.get()
        app_password = self.pass_entry.get()
        to_address = self.to_entry.get()
        subject = self.subject_entry.get()
        body = self.body_text.get("1.0", tk.END)

        # Connect to the SMTP server
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_address, app_password)

        # Create the email message
        message = f"Subject: {subject}\n\n{body}"

        # Send the email
        server.sendmail(from_address, to_address, message)

        # Server clean up
        server.quit()
        self.master.destroy()

root = tk.Tk()
mail_app = MailApp(root)
root.geometry("600x450")
root.mainloop()
