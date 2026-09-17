# Secure User Management System

A cybersecurity-focused Flask web application demonstrating secure user registration, authentication, access control and security monitoring.

## Project Status

This project is currently under development.

### Completed

* [x] Installed and configured Python
* [x] Created an isolated Python virtual environment
* [x] Installed Flask
* [x] Created the initial Flask application
* [x] Added an HTML template
* [x] Successfully ran the application locally
- [x] Installed Flask-SQLAlchemy, Flask-WTF and email-validator
- [x] Created the secure User database model
- [x] Added Scrypt password-hashing methods
- [x] Added user roles and account-lockout fields
- [x] Connected SQLite to the Flask application
- [x] Initialised the local user database


### Planned Security Features

* [ ] User registration
* [ ] Secure login and logout
* [ ] Password hashing
* [ ] Server-side input validation
* [ ] Role-based access control
* [ ] Failed-login monitoring
* [ ] Account lockout
* [ ] Security event logging
* [ ] CSRF protection
* [ ] Security headers
* [ ] Automated security tests
* [ ] OWASP-based security assessment
* [ ] GitHub security scanning

## Technologies

* Python
* Flask
* HTML
* SQLite
* Git and GitHub

## Current Application Structure

```text
secure-user-management-system/
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
└── README.md
```

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

Start the application:

```powershell
flask --app app run --debug
```

Open `http://127.0.0.1:5000` in a browser.

## Security Notice

This project is being developed for educational and portfolio purposes. It uses test accounts and test data only. The Flask development server is not intended for production use.

## Author

Developed by Guyo Guracha, a BSc Cyber Security student at Manchester Metropolitan University.
