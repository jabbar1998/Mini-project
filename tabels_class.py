import Database_methodMAnager
import psycopg2
import datetime



class Department(Database_methodMAnager.Manager):
    def __init__(self, id: int, name: str, phone: str):
        super().__init__('Department', 'id', id, name, phone)
        self.id = id
        self.name = name
        self.phone = phone


class Employee(Database_methodMAnager.Manager):
    def __init__(self, id: int, department: int, account: int, phone: str):
        super().__init__('Employee', 'id', id, department, account, phone)
        self.id = id
        self.department = department
        self.account = account
        self.phone = phone


class Project(Database_methodMAnager.Manager):
    def __init__(self, id: int, department: int, estimated_end_time, title: str, end_time):
        super().__init__('Project', 'id', id, department, estimated_end_time, title, end_time)
        self.id = id
        self.department = department
        self.title = title
        self.estimated_end_time = estimated_end_time
        self.end_time = end_time


class Employeeprojectrelation(Database_methodMAnager.Manager):
    def __init__(self, id: int, employee: int, project: int, hours: int, role: str):
        super().__init__('EmployeeProjectRelation', 'id', id, employee, project, hours, role)
        self.id = id
        self.employee = employee
        self.project = project
        self.hours = hours
        self.role = role


class Attendance(Database_methodMAnager.Manager):
    def __init__(self, id: int, employee: int, date_time: str, in_time: int, out_time: int, late_cause: str):
        super().__init__('Attendance', 'id', id, employee, date_time, in_time, out_time, late_cause)
        self.id = id
        self.employee = employee
        self.date_time = date_time
        self.in_time = in_time
        self.out_time = out_time
        self.late_cause = late_cause


class Salary(Database_methodMAnager.Manager):
    def __init__(self, id: int, employee_id: int, base: float, tax: float, insurance: float, overtime: int):
        super().__init__('Salary', 'id', id, employee_id, base, tax, insurance, overtime)
        self.id = id
        self.employee_id = employee_id
        self.base = base
        self.tax = tax
        self.insurance = insurance
        self.overtime = overtime


class Payslip(Database_methodMAnager.Manager):
    def __init__(self, id: int, base: float, tax: float, insurance: float, overtime: float, created: datetime.date,
                salary_id: int, payment_id: int):
        super().__init__('Payslip', 'payslip_id', id, base, tax, insurance, overtime, created, salary_id, payment_id)
        self.payslip_id = id
        self.base = base
        self.tax = tax
        self.insurance = insurance
        self.overtime = overtime
        self.created = created
        self.salary_idsalary = salary_id
        self.payment_idsalary = payment_id

class Payment(Database_methodMAnager.Manager):
    def __init__(self, id: int, amount: float, number_account: str, type_payment: str, description: str,
                date=datetime.datetime.now()):
        super().__init__('Payment', 'Payment_id', id, amount, number_account, type_payment, description, date)
        self.Payment_id = id
        self.amount = amount
        self.number_account = number_account
        self.type_payment = type_payment
        self.description = description
        self.date = date
