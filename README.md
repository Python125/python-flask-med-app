# python-flask-med-app

Welcome to my Medication Reminder project! This Python application, built on the Flask framework, helps users manage their medication schedules through timely email reminders. To get the best experience of this GitHub repository, be sure to follow the step-by-step instructions outlined below. I developed this project using Visual Studio Code as my source-code editor and Ubuntu (Linux) as my operating system. If you’re using Windows 11, you’ll find the relevant commands included in the instructions.

# Instructions:
Assuming you already have a GitHub account, use Visual Studio Code, have a Google account, and have already cloned my repository:
1. Activate a virtual environment: In order to get the best experience of this GitHub repository, you need to activate a virtual environment in Visual Studio Code. This will isolate any project dependencies by ensuing they don’t interfere with other projects or systems.

Here are the commands to complete this step (only execute one command at a time):

> Linux (Ubuntu):

- python3 -m venv venv

- source venv/bin/activate

> Windows 11:

- py -m venv venv

- Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

- .\venv\Scripts\Activate

2. Go to your google account and click on your profile. It should have a button that says "Manage your Google Account".

3. Once you click that button, you need to go to "Security". Once you are there, go to "2-Step Verification". You need to enter your mobile phone number to verify. Once you do that, 2-Step Verification should be enabled.

4. Scroll down to the bottom of the "2-Step Verification" page, and you should see an "App passwords" section.

5. Create an .env file in Visual Studio Code. This is IMPORTANT.

6. Go to "App passwords", and add the name of your app in the text box. An app password should be given to you. DO NOT share this with ANYONE. Copy the password and place it somewhere PRIVATE AND SAFE such as an .env file. MAKE SURE IT LOOKS EXACTLY LIKE THE PASSWORD GOOGLE PROVIDED. 
- YOU WILL NOT BE ABLE TO SEE THE PASSWORD FROM GOOGLE AFTER COPYING IT.

7. In the "med_reminder.py" and "tasks.py" files, paste the SAME email that you have used to obtain the Google app password from the "2-Step Verification" section. So for example, if you used the email "dan@gmail.com" to obtain the Google app password, you would use that email and paste it into those two files where indicated.

> med_reminder.py:

- self.email_label = tk.Label(master, text="recipient_email@gmail.com")

- server.sendmail(email, 'recipient_email@gmail.com', f'Subject: Medicine Reminder\n\nIt\'s time to take your {medicine_name}!')

> tasks.py:

- server.sendmail(email, 'recipient_email@gmail.com', f'Subject: Medicine Reminder\n\nIt\'s time to take your {medicine_name}!')

8. In the "med_reminder.py" file, paste the app password you received from the "2-Step Verification" section. Wherever you saved it from

10. Make sure you have two terminals up at the same time.

In each terminal, activate the virtual environment and then run one of the following commands based on the terminal like this:

Terminal 1:
    python3 app.py

Terminal 2:
    python3 celery_worker.py