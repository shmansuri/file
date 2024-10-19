Project Overview
Web Page Creation: A Django web page that allows users to upload Excel/CSV files.
Summary Report: The app processes the uploaded file and generates a summary report based on the data.
Email Notification: The summary report is emailed to the specified recipient.
Deployment: The application can be deployed on an open-source server like Heroku.
GitHub Integration: Push your changes to a separate branch created with your name.
Features
File upload support for Excel/CSV formats.
Automated generation of data summary (e.g., column-wise count, mean, and standard deviation).
Email the summary report directly to a specified email address.
Can be deployed on Heroku or similar platforms.
Full GitHub integration for version control.
Technologies Used
Django - Web framework
Python - Core language
Pandas - For data processing
OpenPyXL - To handle Excel files
Heroku - Deployment platform
Gmail SMTP - For email functionality
Getting Started
Follow the instructions below to get a copy of the project up and running on your local machine.

Prerequisites
Ensure you have the following installed:

Python 3.8 or higher
Django 4.0 or higher
Virtual environment tool (optional but recommended)
Heroku CLI (for deployment)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/repository-name.git
Navigate into the project directory:

bash
Copy code
cd repository-name
Create and activate a virtual environment:

bash
Copy code
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Set up your environment variables. Create a .env file in the root directory and add your secret key and email configuration:

bash
Copy code
SECRET_KEY=your-secret-key
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-email-password
Run migrations:

bash
Copy code
python manage.py migrate
Start the development server:

bash
Copy code
python manage.py runserver
Open your browser and go to http://127.0.0.1:8000/ to access the application.

Usage
Upload an Excel/CSV file via the web page.
The application will generate a summary report based on the uploaded data.
The summary will be emailed to the specified email address (configured in the .env file).
Git Workflow
Create a new branch with your name:

bash
Copy code
git checkout -b your-name-branch
Add and commit your changes:

bash
Copy code
git add .
git commit -m "Your commit message"
Push your branch to the repository:

bash
Copy code
git push origin your-name-branch
Deployment on Heroku
Login to Heroku:

bash
Copy code
heroku login
Create a new Heroku app:

bash
Copy code
heroku create your-app-name
Add Heroku as a remote repository:

bash
Copy code
heroku git:remote -a your-app-name
Deploy your app:

bash
Copy code
git push heroku your-name-branch:master
Run migrations on Heroku:

bash
Copy code
heroku run python manage.py migrate
Open your application:

bash
Copy code
heroku open
Email Configuration
The application uses Gmail SMTP for sending emails. Set the following environment variables in your .env file:

bash
Copy code
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-email-password
Make sure to replace the placeholder values with your actual email credentials.

Summary Report Example
The summary report generated from the uploaded Excel/CSV file will include basic statistical data like count, mean, and standard deviation for each column.

Column Name	Count	Mean	Std Dev
Example Col1	100	50	5
Example Col2	100	35	8
Contributing
