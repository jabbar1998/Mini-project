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
            result = Database_methodMAnager.Manager.filter(table_name, **kwargs)
            print(result)
        case '5':
            Permission2 = True
            break

while Permission2:
    print('''
    Please choice:
    1.total_dept  
    2.See Object
    3.Delet in the Tabel
    4.Save in the Table
    5.Exit
        ''')
    value = input('Enter: ')
    match value:
        case '1':
            print(task5.total_dept())
        case '2':
            x=int(input("Enter Hours: "))
            print(task5.total_overtime(x))
        case '3':
            
    