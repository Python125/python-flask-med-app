import tkinter as tk
from datetime import datetime, timedelta
from plyer import notification
import smtplib

class MedicineReminderApp:
    def __init__(self, master):
        self.master = master
        master.title("Medicine Reminder App")

        # Label and Entry for Email
        self.email_label = tk.Label(master, text="recipient_email@gmail.com")
        self.email_label.pack()

        self.email_entry = tk.Entry(master)
        self.email_entry.pack()

        # Label and Entry for Password
        self.password_label = tk.Label(master, text="5gkw lwp3 sD2h 0iqJ")
        self.password_label.pack()

        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()

        # Label and Entry for Medicine Name
        self.medicine_name_label = tk.Label(master, text="Medicine Name:")
        self.medicine_name_label.pack()

        self.medicine_name_entry = tk.Entry(master)
        self.medicine_name_entry.pack()

        # Label and Entry for Reminder Time
        self.reminder_time_label = tk.Label(master, text="Reminder Time (YYYY-MM-DD HH:MM):")
        self.reminder_time_label.pack()

        self.reminder_time_entry = tk.Entry(master)
        self.reminder_time_entry.pack()

        # Button to Schedule Reminder
        self.schedule_button = tk.Button(master, text="Schedule Reminder", command=self.schedule_notification)
        self.schedule_button.pack()

    def schedule_notification(self):
        medicine_name = self.medicine_name_entry.get()
        reminder_time_str = self.reminder_time_entry.get()

        # Convert the reminder_time_str to a datetime object
        reminder_time = datetime.strptime(reminder_time_str, "%Y-%m-%d %H:%M")

        # Calculate the time difference between now and the reminder time
        time_difference = reminder_time - datetime.now()

        # Schedule the notification
        self.master.after(int(time_difference.total_seconds() * 1000), self.show_notification, medicine_name)

    def show_notification(self, medicine_name):
        notification_title = "Medicine Reminder"
        notification_message = f"It's time to take your {medicine_name}!"

        notification.notify(
            title=notification_title,
            message=notification_message,
            app_icon=None,  # e.g., 'C:\\icon_32x32.ico'
            timeout=10,  # seconds
        )

        # Send email notification
        self.send_email_notification(medicine_name)

    def send_email_notification(self, medicine_name):
        email = self.email_entry.get()
        password = self.password_entry.get()

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(email, password)

            # Replace 'recipient_email@gmail.com' with the recipient's email address
            server.sendmail(email, 'recipient_email@gmail.com', f'Subject: Medicine Reminder\n\nIt\'s time to take your {medicine_name}!')

# Create the main Tkinter window
root = tk.Tk()

# Create an instance of the MedicineReminderApp
app = MedicineReminderApp(root)

# Run the Tkinter main loop
root.mainloop()
