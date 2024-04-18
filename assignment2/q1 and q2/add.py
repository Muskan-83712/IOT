import dbconn
empid = int(input("Enter the employee id: "))
name = input("Enter name of employee: ")
department = input("Enter department of employee: ")
email = input("Enter the email of employee:")
salary = float(input("Enter the salary of employee: "))
date_of_joining = input("Enter the date of joining: ")

def add_info():
    conn = dbconn.get_connection()
    query = f"insert into employee_info values({empid},'{name}','{department}','{email}',{salary},'{date_of_joining}');"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
    
add_info()
