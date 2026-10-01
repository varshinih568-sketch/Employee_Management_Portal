from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employees.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(20), unique=True, nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    designation = db.Column(db.String(100), nullable=False)
    joining_date = db.Column(db.String(20), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    employment_status = db.Column(db.String(20), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():

    search = request.args.get("search", "")
    status = request.args.get("status", "")

    employees = Employee.query.all()

    # Dashboard counts
    total_employees = len(employees)

    active_employees = len(
        [e for e in employees if e.employment_status == "Active"]
    )

    on_leave_employees = len(
        [e for e in employees if e.employment_status == "On Leave"]
    )

    resigned_employees = len(
        [e for e in employees if e.employment_status == "Resigned"]
    )

    # Search filter
    if search:
        search = search.lower().strip()

        employees = [
            employee for employee in employees
            if search in employee.employee_id.lower()
            or search in employee.full_name.lower()
            or search in employee.email.lower()
            or search in employee.phone.lower()
            or search in employee.department.lower()
            or search in employee.designation.lower()
            or search in employee.location.lower()
            or search in employee.employment_status.lower()
        ]

    # Status filter
    if status:
        employees = [
            employee for employee in employees
            if employee.employment_status.strip().lower()
            == status.strip().lower()
        ]

    return render_template(
        "index.html",
        employees=employees,
        search=search,
        status=status,
        total_employees=total_employees,
        active_employees=active_employees,
        on_leave_employees=on_leave_employees,
        resigned_employees=resigned_employees
    )


@app.route("/add", methods=["GET", "POST"])
def add_employee():

    if request.method == "POST":

        employee = Employee(
            employee_id=request.form["employee_id"],
            full_name=request.form["full_name"],
            email=request.form["email"],
            phone=request.form["phone"],
            department=request.form["department"],
            designation=request.form["designation"],
            joining_date=request.form["joining_date"],
            salary=request.form["salary"],
            location=request.form["location"],
            employment_status=request.form["employment_status"]
        )

        db.session.add(employee)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("add_employee.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_employee(id):

    employee = Employee.query.get_or_404(id)

    if request.method == "POST":

        employee.employee_id = request.form["employee_id"]
        employee.full_name = request.form["full_name"]
        employee.email = request.form["email"]
        employee.phone = request.form["phone"]
        employee.department = request.form["department"]
        employee.designation = request.form["designation"]
        employee.joining_date = request.form["joining_date"]
        employee.salary = request.form["salary"]
        employee.location = request.form["location"]
        employee.employment_status = request.form["employment_status"]

        db.session.commit()

        return redirect(url_for("home"))

    return render_template(
        "edit_employee.html",
        employee=employee
    )


@app.route("/delete/<int:id>", methods=["POST"])
def delete_employee(id):

    employee = Employee.query.get_or_404(id)

    db.session.delete(employee)
    db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)