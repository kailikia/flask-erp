from payroll import *
from payrollCalculator import PayrollCalculator
from flask import Flask,render_template,request,redirect,url_for
import requests
from requests.auth import HTTPBasicAuth


app = Flask(__name__)

auth = HTTPBasicAuth('mse', 'ficha123')


@app.route("/")
def home():
    url = "http://127.0.0.1:5000/api/employees/"
    response = requests.get(url, auth=auth)
    print('my rrespo',response.json())

    allEmployees = Employee.select()
    return render_template("index.html", displayEmployees = allEmployees)

@app.route("/employee")
def employee():
    return render_template("addEmployee.html")
#
# @app.route("/saveEmployee",methods=["POST"])
# def saveEmployee():
#     name = request.form["form_full_name"]
#     kra = request.form["form_kra_pin_number"]
#     department =request.form['form_department']
#     position = request.form['form_position']
#     basic = request.form['form_basic_salary']
#     house = request.form['form_house_allowance']
#
#     Employee.create(full_name= name,
#                     kra_pin_number=kra,
#                     department=department,
#                     position=position,
#                     basic_salary=basic,
#                     house_allowance=house)
#     return redirect(url_for("home"))
#
# @app.route("/updateEmployee/<me>", methods=["POST"])
# def update(me):
#     #Fetch the Employer using their Id
#     emp = Employee.select().where(Employee.id == int(me)).get()
#     #Update the Employee Details
#     emp.full_name = request.form["form_full_name"]
#     emp.kra_pin_number = request.form["form_kra_pin_number"]
#     emp.department = request.form['form_department']
#     emp.position = request.form['form_position']
#     emp.basic_salary = request.form['form_basic_salary']
#     emp.house_allowance = request.form['form_house_allowance']
#     emp.save()
#     return redirect(url_for("home"))
#
# @app.route("/deleteEmployee/<me>",methods=["GET"])
# def delete(me):
#     emp = Employee.select().where(Employee.id == int(me)).get()
#     emp.delete_instance()
#     return redirect(url_for("home"))
#
# #Payroll routes
#
# @app.route("/payroll/<m>")
# def payroll(m):
#   allPayrolls = Payroll.select().join(Employee).where(Employee.id == int(m))
#   return render_template("payroll.html", myPayrolls = allPayrolls, employeeId = m)
#
# @app.route("/payroll/add", methods=["POST"])
# def payrollAdd():
#     overtime = request.form["form_overtime"]
#     benefits = request.form["form_other_benefits"]
#     payrollDate = request.form['form_payroll_date']
#     employee_id = request.form['form_emp_id']
#
#     emp = Employee.select().where(Employee.id == int(employee_id)).get()
#
#     calc = PayrollCalculator(emp.basic_salary,overtime,5235,benefits)
#
#     Payroll.create(overtime = overtime,
#                    other_benefits = benefits,
#                    nhif = calc.nhif,
#                    nssf = calc.nssf,
#                    payee = calc.payee,
#                    employee_id = employee_id,
#                    payroll_date = payrollDate)
#
#     return redirect(url_for("payroll", m =employee_id))


if __name__ == "__main__":
    app.run(port=5001)