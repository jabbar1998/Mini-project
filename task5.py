from Database_methodMAnager import Database

def total_dept():
    with Database() as conn:
        with conn.cursor() as cur:
            cur.execute("""SELECT SUM(base+tax+insurance+overtime)
                            FROM payslip WHERE payment IS NULL;""")
            result = cur.fetchone()
    return f'"total_dept": {result[0]}'

def total_overtime(x):
    with Database() as conn:
        with conn.cursor() as cur:    
            cur.execute(f"""SELECT SUM(payslip.overtime) FROM payslip
                            JOIN salary ON salary.id=payslip.salary
                            WHERE salary.overtime >= {x} AND payslip.payment IS NOT NULL;""")
            result = cur.fetchone()
    return f'"total_overtime": {result[0]}'

def total_pay():
    with Database() as conn:
        with conn.cursor() as cur:
            cur.execute("""SELECT SUM(amount) FROM payment;""")
            result = cur.fetchone()
    return f'"total_pay": {result[0]}'

def total_hours(x):
    with Database() as conn:
        with conn.cursor() as cur:
            cur.execute(f"""SELECT SUM(hours) FROM employeeprojectrelation
                            WHERE employee = {x};""")
            result = cur.fetchone()
    return f'"total_hours": {result[0]}'


def employee_upper_pay(x):
    with Database() as conn:
        with conn.cursor() as cur:
            cur.execute(f"""WITH emp AS (
                            SELECT salary.employee, SUM(PA.amount)AS total_amount FROM salary
                            JOIN payslip P ON salary.id = P.salary
                            JOIN payment PA ON P.payment = PA.id
                            GROUP BY salary.employee)
                            SELECT employee.id,emp.total_amount FROM employee
                            JOIN emp ON emp.employee=employee.id WHERE total_amount > {x};""")
            result=cur.fetchall()
    return result

def employee_max_work():
    with Database() as conn:
        with conn.cursor() as cur:
            cur.execute("""WITH emp AS (
                            SELECT employee,SUM(hours) FROM employeeprojectrelation
                            GROUP BY employee)
                            SELECT employee.id,emp.sum FROM employee
                            JOIN emp ON emp.employee=employee.id
                            WHERE emp.sum=(SELECT MAX(sum) FROM emp)
                            ORDER BY employee.id DESC LIMIT 1;
                            """)
            result=cur.fetchone()
    return result

def department_max_pay():
    with Database() as conn:
        with conn.cursor() as cur:
            cur.execute("""WITH department_totals AS (
                        SELECT DISTINCT D.id AS department, SUM(P2.amount) AS total_payment FROM department D
                        JOIN employee E ON D.id = E.department
                        JOIN salary S ON E.id = S.employee
                        JOIN payslip P ON S.id = P.salary
                        JOIN payment P2 ON P2.id = P.payment
                        GROUP BY D.id)SELECT D.id,D.name,D.phone,D1.total_payment AS max_total FROM department_totals D1
                        JOIN department D ON D.id = D1.department
                        WHERE D1.total_payment = (SELECT MAX(total_payment) FROM department_totals)
                        ORDER BY D.name LIMIT 1;
                        """)
            result=cur.fetchone()
    return result

def on_time_department():
    with Database() as conn:
        with conn.cursor() as cur:
            cur.execute("""SELECT D.name,SUM(P.estimated_end_time-P.end_time) AS delta
                            FROM department D
                            JOIN project P on D.id = P.department
                            GROUP BY D.name
                            ORDER BY delta DESC, D.name LIMIT 1;
                            """)
            result=cur.fetchone()[0]
    return result


def employee_min_late(x):
    with Database() as conn:
        with conn.cursor() as cur:
            cur.execute(f"""WITH att AS (
                            SELECT E.id,(EXTRACT(
                            EPOCH FROM A.in_time - '{x}') * INTERVAL '1 second')::INTERVAL AS time_diff
                            FROM employee E
                            JOIN attendance A ON E.id = A.employee
                            WHERE (EXTRACT(
                            EPOCH FROM A.in_time - '{x}') * INTERVAL '1 second')::INTERVAL > '00:00:00'::INTERVAL
                            ORDER BY time_diff)
                            SELECT employee.id,COUNT(att.time_diff) FROM employee
                            JOIN att ON att.id=employee.id
                            GROUP BY employee.id,att.id
                            ORDER BY count , employee.id LIMIT 1;
                            """)
            result = cur.fetchone()
    return result[0]

def unemployed_count():
    with Database() as conn:
        with conn.cursor() as cur:
            cur.execute("""SELECT COUNT(E.id) FROM employee E
                        WHERE E.id NOT IN (
                        SELECT employee FROM employeeprojectrelation);
                        """)
            result=cur.fetchone()[0]
    return f'"total": {result}'

print(total_dept())
print(total_overtime(10))
print(total_pay())
print(total_hours(115))
print(employee_upper_pay(2000))
print(employee_max_work())
print(department_max_pay())
print(on_time_department())
print(employee_min_late('09:00:00'))
print(unemployed_count())