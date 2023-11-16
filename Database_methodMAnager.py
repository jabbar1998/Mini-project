import psycopg2


class Database:
    def __enter__(self):
        self.conn = psycopg2.connect(
            host='94.101.187.206',
            dbname='jabardb',
            user='jabar',
            password='jabbar1998%',
            port=5432
        )
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

class Manager:
    def __init__(self, table_name):
        self.table_name = table_name
        # self.id_col = id_col

    @classmethod
    def get(cls,table_name, **kwargs) :
        try:
            with Database() as conn:
                with conn.cursor() as cur:
                    condithions = [f"{col} = %s" for col in kwargs.keys()]
                    values = tuple(kwargs.values()) 
                    query = f"select * from {table_name} WHERE {' AND '.join(condithions)}"
                    cur.execute(query,values)
                    result = cur.fetchall()
                    return result
        except Exception as error:
            return f"You have error {error}"

    @classmethod
    def filter(cls,table_name, **kwargs):
        try:
            with Database() as conn:
                with conn.cursor() as cur:
                    condithions = [f"{col} = %s" for col in kwargs.keys()]
                    values = tuple(kwargs.values())
                    query = f"select * from {table_name} WHERE {' AND '.join(condithions)}"
                    cur.execute(query,values)
                    result = cur.fetchall()
                    obj = cls(*result)
                    return obj
        except Exception as error:
            return f"You have error {error}"

    @classmethod
    def delet(cls,table_name, **kwargs):
        try:
            with Database() as conn:
                with conn.cursor() as cur:
                    if not kwargs:
                        return f"The Valuse Is Incorrect! ."
                    else:
                        condithions = [f"{col} = %s" for col in kwargs.keys()]
                        values = tuple(kwargs.values())
                        query = f"DELETE FROM {table_name} CASCADE WHERE {' AND '.join(condithions)} "
                        cur.execute(query,values)
                        return f"The Delet Is Successful! ."
        except Exception as error:
            return f"You have error {error}"

    @classmethod    
    def save(cls,table_name,**kwargs):
        try:
            with Database() as conn:
                with conn.cursor() as cur:
                    columns = (', ').join(kwargs.keys())
                    values = (', ').join(['%s']*len(kwargs))
                    query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
                    cur.execute(query,tuple(kwargs.values()))
                    conn.commit()
                    print (f"{table_name} is Add! .")
        except Exception as error:
            print( f"You have error {error}")

def create():
    try:
        with Database() as conn:
            with conn.cursor() as cur:
                query='''
CREATE TABLE Department (
    id bigINT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(11)
);

CREATE TABLE Employee (
    id bigINT PRIMARY KEY,
    department BIGINT,
    account bigINT,
    phone VARCHAR(11),
    FOREIGN KEY (department) REFERENCES Department (id) ON DELETE CASCADE
);

CREATE TABLE Project (
    id bigINT PRIMARY KEY,
    department INTEGER,
    title VARCHAR(100),
    estimated_end_time date,
    end_time date,
    FOREIGN KEY (department) REFERENCES Department (id) ON DELETE CASCADE
);

CREATE TABLE EmployeeProjectRelation (
    id bigINT PRIMARY KEY,
    employee BIGINT,
    project BIGINT,
    hours INTeGER,
    role VARCHAR(100),
    FOREIGN KEY (employee) REFERENCES Employee (id) ON DELETE CASCADE,
    FOREIGN KEY (project) REFERENCES Project (id) ON DELETE CASCADE
);

CREATE TABLE Attendance (
    id bigINT PRIMARY KEY,
    employee BIGINT,
    date DATE,
    in_time time,
    out_time time,
    late_cause VARCHAR(250),
    FOREIGN KEY (employee) REFERENCES Employee (id) ON DELETE CASCADE
);

CREATE TABLE Salary (
    id bigINT PRIMARY KEY,
    employee BIGINT,
    base decimal,
    tax decimal,
    insurance decimal,
    overtime INTeGER,
    FOREIGN KEY (employee) REFERENCES Employee (id) ON DELETE CASCADE
);

CREATE TABLE Payment (
    id bigINT PRIMARY KEY,
    amount decimal,
    account_number VARCHAR(20),
    payment_type VARCHAR(1),
    description VARCHAR(100),
    date DATE
);

CREATE TABLE Payslip (
    id bigINT PRIMARY KEY,
    base decimal,
    tax decimal,
    insurance decimal,
    overtime decimal,
    created date,
    salary BIGINT,
    payment BIGINT,
    FOREIGN KEY (payment) REFERENCES Payment (id) ON DELETE CASCADE,
    FOREIGN KEY (salary) REFERENCES Salary (id) ON DELETE CASCADE
);
'''
                cur.execute(query)
                conn.commit()
                return f'Tables is Create! .'
            
    except Exception as error:
        return f'You have Error : {error}'