import psycopg2
import tabels_class
import json
import Database_methodMAnager
import task5

Permission1 = False
Permission2 = False

while True:
    print('You Must Create Table')
    n = input("Please Enter 'y' To Create Table: ")
    print(n)
    if n == 'y':
        print(Database_methodMAnager.create())
        print('You Must Add jsone File To database ')
        m = input("Please Enter 'y' To Add jsone File To database: ")
        if m == 'y':
            with open('data_sample.json', '+r') as file:
                data = json.load(file)
                for name in data:
                    model_class = ((name['model'])[8:]).capitalize()
                    kwargs = {"id": name['pk'], **name['fields']}
                    try:
                        Database_methodMAnager.Manager.save(model_class, **kwargs)
                        Permission1 = True
                    except Exception as e:
                        print(e)
                        Permission1 = False
            break            
        elif m == 'n':
            Permission1 = True
            break
        else:
            raise 'Please Enter Courrect input! .'
    else:
        raise 'Please Enter Courrect input! .'

while Permission1:
    print('''
    Please choice:
    1.See with eleman  
    2.See Object
    3.Delet in the Tabel
    4.Save in the Table
    5.Exit
        ''')
    value = input('Enter: ')
    if value=='5':
        Permission2 = True
        break
    print('Explane : pk:value1 , phone:value2 ...')
    table_name = input("Enter table name: ")
    user_input = input("Enter column and value pairs (e.g. column1:value1, column2:value2): ").strip()
    kwargs = dict(item.split(':') for item in user_input.split(','))
    match value:
        case '1':
            result = Database_methodMAnager.Manager.get(table_name, **kwargs)
            print(result[0])
        case '2':
            result = Database_methodMAnager.Manager.filter(table_name, **kwargs)
            print(result)
        case '3':
            result = Database_methodMAnager.Manager.delet(table_name, **kwargs)
            print(result)
        case '4':
            result = Database_methodMAnager.Manager.save(table_name, **kwargs)
            print(result)

while Permission2:
    print('''
    Please choice:
    1.total_dept  
    2.total_overtime
    3.total_pay
    4.total_hours
    5.employee_upper_pay
    6.employee_max_work
    7.department_max_pay
    8.on_time_department
    9.employee_min_late
    10.unemployed_count
        ''')
    value = input('Enter: ')
    match value:
        case '1':
            print(task5.total_dept())
        case '2':
            x=10
            print(task5.total_overtime(x))
        case '3':
            print(task5.total_pay)
        case '4':
            x=115
            print(task5.total_hours(x))
        case '5':
            x=2000
            print(task5.employee_upper_pay(x))
        case '6':
            print(task5.employee_max_work)
        case '7':
            print(task5.department_max_pay)   
        case '8':
            x=int(input("Enter: "))
            print(task5.employee_min_late(x))
        case '9':
            x='09:00:00'
            print(task5.employee_min_late(x))
        case '10':
            print(task5.unemployed_count)