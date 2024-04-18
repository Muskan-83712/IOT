
import dbconn

def switch(opr):
    match opr:
        case 1:
            return add_info()
        case 2:
            return update_emp_info(4,70000)
        case 3:
            return delete_emp_info(3)
        
    

def add_info():
    conn = dbconn.get_connection()
    empid = int(input("Enter the employee id: "))
    name = input("Enter name of employee: ")
    department = input("Enter department of employee: ")
    email = input("Enter the email of employee:")
    salary = float(input("Enter the salary of employee: "))
    date_of_joining = input("Enter the date of joining: ")
    query = f"insert into employee_info values({empid},'{name}','{department}','{email}',{salary},'{date_of_joining}');"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

def update_emp_info(empid,salary):
    conn = dbconn.get_connection()
    query = f"update employee_info SET salary = %s where empid = %s;"
    val = (salary, empid)
    cursor = conn.cursor()
    cursor.execute(query, val)
    conn.commit()
    cursor.close()
    conn.close()

def delete_emp_info(empid):
    conn = dbconn.get_connection()
    query = f"delete from employee_info where empid = %s;"
    val = (empid, )
    cursor = conn.cursor()
    cursor.execute(query, val)
    conn.commit()
    cursor.close()
    conn.close()

head = switch(1)
print(head)
head = switch(2)
print(head)
head = switch(3)
print(head)