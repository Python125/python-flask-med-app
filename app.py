from flask import Flask, render_template, request
from celery import Celery
from tasks import send_task_notification
from datetime import datetime

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(
    app.import_name,
    backend=app.config['CELERY_RESULT_BACKEND'],
    broker=app.config['CELERY_BROKER_URL']
)
celery.conf.update(app.config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule_task', methods=['POST'])
def schedule_task():
    email = request.form.get('email')
    password = request.form.get('password')
    medicine_name = request.form.get('medicine_name')
    reminder_time_str = request.form.get('reminder_time')

    # Convert the reminder_time_str to a datetime object
    reminder_time = datetime.strptime(reminder_time_str, "%Y-%m-%d %H:%M")

    # Schedule the Celery task
    send_task_notification.apply_async(args=[email, password, medicine_name, reminder_time], countdown=(reminder_time - datetime.now()).total_seconds())

    return "Task scheduled successfully!"

if __name__ == '__main__':
    app.run(debug=True)