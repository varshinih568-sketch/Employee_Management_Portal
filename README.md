# Employee Management Portal

A web-based Employee Management Portal developed using Flask and SQLite.  
This project provides a simple system for managing employee information through a user-friendly web interface.

## Features

- Add new employees
- View employee records
- Edit employee information
- Manage employee details
- Delete employee records
- Employee database using SQLite
- Responsive web interface

## Employee Information

The system manages details such as:

- Employee ID
- Full Name
- Email
- Phone
- Department
- Designation
- Joining Date
- Salary
- Location
- Employment Status

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML
- CSS

## Project Structure

```text
Employee_Management_Portal/
│
├── app.py
├── instance/
│   └── employees.db
│
├── static/
│   └── css/
│       └── style.css
│
└── templates/
    ├── index.html
    ├── employees.html
    ├── add_employee.html
    └── edit_employee.html
