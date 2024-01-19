# python-flask-med-app

Welcome to my Medication Reminder project! This Python application, built on the Flask framework, helps users manage their medication schedules through timely email reminders. To get the best experience of this GitHub repository, be sure to follow the step-by-step instructions outlined below. I developed this project using Visual Studio Code as my source-code editor and Ubuntu (Linux) as my operating system. If you’re using Windows 11, you’ll find the relevant commands included in the instructions.

# Instructions:
- DO NOT PUSH ANY CHANGES TO YOUR GITHUB ACCOUNT UNTIL YOU COMPLETE THESE STEPS FIRST. This is crucial for security reasons and to prevent the loss or misuse of your personal information.

Assuming you have a GitHub account, use Visual Studio Code, possess a Google account, and have cloned my repository:
1. Activate a virtual environment: To enhance your experience with this GitHub repository, activate a virtual environment in Visual Studio Code. This ensures isolation of project dependencies, preventing interference with other projects or systems.

Here are the commands to complete this step (only execute one command at a time):

> Linux (Ubuntu):

- python3 -m venv venv

- source venv/bin/activate

> Windows 11:

- py -m venv venv

- Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

- .\venv\Scripts\Activate

2. Install the necessary frameworks, libraries, or packages to the project. For this project, you need to install celery, redis, flask, plyer, and tkinter.

> Command to install dependencies:
- pip install flask celery redis plyer tkinter

- If additional frameworks, libraries, or packages need installation, you'll notice a yellow squiggly line under that name.

3. On the upper right corner is your Google profile picture. Click on it, then once you do, you should see a button that says "Manage your Google Account".

4. After clicking the "Manage your Google Account" button, navigate to "Security". Within the Security section, access "2-Step Verification". Enter your mobile phone number for verification, and once completed, "2-Step Verification" will be enabled.

5. Scroll to the bottom of the "2-Step Verification" page to find the "App passwords" section.

6. Create an .env file in Visual Studio Code. This step is CRUCIAL.

7. In the "App passwords" section, enter your app's name in the text box. A unique app password will be generated for you. DO NOT share this password with anyone. Copy the password and securely store it in a private location, such as an .env file.
- IMPORTANT: Ensure that the copied password matches EXACTLY with the one provided by Google. Accuracy is CRUCIAL.

- IMPORTANT: YOU WILL NOT BE ABLE TO SEE THE PASSWORD FROM GOOGLE AFTER COPYING IT.

8. In the "med_reminder.py" and "tasks.py" files (located in the root directory), paste the SAME email you used to obtain the Google app password in the "2-Step Verification" section. For instance, if you used the email "mal@gmail.com" for the Google app password, paste that email into the designated sections in both files.

> med_reminder.py:

- line 12: self.email_label = tk.Label(master, text="recipient_email@gmail.com")

- line 79: server.sendmail(email, 'recipient_email@gmail.com', f'Subject: Medicine Reminder\n\nIt\'s time to take your {medicine_name}!')

> tasks.py:

- line 27: server.sendmail(email, 'recipient_email@gmail.com', f'Subject: Medicine Reminder\n\nIt\'s time to take your {medicine_name}!')

9. In the "med_reminder.py" file, paste the app password obtained from the "2-Step Verification" section in your .env file. Copy the password and insert it into the designated section in the "med_reminder.py" file.

> med_reminder.py:
- line 19: self.password_label = tk.Label(master, text="PASTE_GOOGLE_APP_PASSWORD_HERE")

10. Ensure you have two terminals open simultaneously. In each terminal, activate the virtual environment, and then run one of two commands listed below in each terminal:

> Terminal 1:
- python3 app.py

> Terminal 2:
- python3 celery_worker.py

11. After activating the virtual environment in both terminals and running "app.py" and "celery_worker.py", you can input information into the text boxes within the app. Complete details such as email, app password, medication name, and reminder time. Click the "Schedule Reminder" button, and you should be directed to a new page displaying "Task scheduled successfully!".