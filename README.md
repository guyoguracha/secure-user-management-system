# Secure User Management System

A cybersecurity-focused Flask web application demonstrating secure user registration, authentication, access control and security monitoring.

## Project Status

This project is currently under development.

### Completed

* [x] Installed and configured Python
* [x] Created an isolated Python virtual environment
* [x] Installed Flask
* [x] Created the initial Flask application
* [x] Added HTML templates
* [x] Successfully ran the application locally
* [x] Installed Flask-SQLAlchemy, Flask-WTF and email-validator
* [x] Created the secure User database model
* [x] Connected SQLite to the Flask application
* [x] Initialised the local user database
* [x] Added secure environment-variable support
* [x] Created a user registration form
* [x] Added server-side input validation
* [x] Prevented duplicate usernames and email addresses
* [x] Added CSRF protection
* [x] Added Scrypt password hashing

### Security Features

* [x] User registration
* [ ] Secure login and logout
* [x] Password hashing
* [x] Server-side input validation
* [ ] Role-based access control
* [ ] Failed-login monitoring
* [ ] Account lockout
* [ ] Security event logging
* [x] CSRF protection
* [ ] Security headers
* [ ] Automated security tests
* [ ] OWASP-based security assessment
* [ ] GitHub security scanning

## Technologies

* Python
* Flask
* Flask-SQLAlchemy
* Flask-WTF
* SQLite
* HTML
* Git and GitHub

## Current Application Structure

```text
secure-user-management-system/
├── instance/
│   └── users.db
├── templates/
│   ├── index.html
│   └── register.html
├── .env
├── .gitignore
├── app.py
├── forms.py
├── models.py
├── README.md
└── requirements.txt
```

The `.env`, `.venv`, `instance` and `__pycache__` files and folders are excluded from Git to protect sensitive or local data.

## Running the Project Locally

Create and activate a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the required packages:

```powershell
py -m pip install -r requirements.txt
```

Generate a secure secret key:

```powershell
py -c "import secrets; print(secrets.token_hex(32))"
```

Create a private `.env` file in the main project folder:

```env
SECRET_KEY=your_generated_secret_key
```

Initialise the database:

```powershell
flask --app app init-db
```

Start the application:

```powershell
flask --app app run --debug
```

Open the following pages:

```text
Home: http://127.0.0.1:5000
Registration: http://127.0.0.1:5000/register
```

## Security Measures Implemented

* Passwords are hashed using Scrypt and are never stored as plain text.
* Registration forms use CSRF protection.
* User input is validated on the server.
* Usernames and email addresses must be unique.
* The Flask secret key is stored in a private environment file.
* The local database and environment file are excluded from Git.

## Security Notice

This project is being developed for educational and portfolio purposes. It uses test accounts and test data only. The Flask development server is not intended for production use.

## Author

Developed by **Guyo Guracha**, a BSc Cyber Security student at Manchester Metropolitan University.
