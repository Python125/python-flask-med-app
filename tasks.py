from celery import Celery
from plyer import notification
import smtplib

celery = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

@celery.task
def send_task_notification(email, password, medicine_name, reminder_time):

    notification_title = "Medicine Reminder"
    notification_message = f"It's time to take your {medicine_name}!"

    notification.notify(
        title=notification_title,
        message=notification_message,
        app_icon=None,
        timeout=10,
    )

    send_email_notification(email, password, medicine_name)

def send_email_notification(email, password, medicine_name):
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(email, password)

        server.sendmail(email, 'recipient_email@gmail.com', f'Subject: Medicine Reminder\n\nIt\'s time to take your {medicine_name}!')
