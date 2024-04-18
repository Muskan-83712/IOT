import dbconn


def read_emp_info():
    conn = dbconn.get_connection()
    query1 = f"select *from employee_info;"
    query3 = f"select name,salary from employee_info order by salary DESC LIMIT 1;"
    query4 = f"select name ,salary from employee_info order by salary ASC LIMIT 1;"
    cursor = conn.cursor()
    
    print("ALL Employee")
    cursor.execute(query1)
    records = cursor.fetchall()
    for ele in records:
        print(ele)

    print("")
    print("employee with selected department")
    department = input("Enter department: ")
    query2 = f"select name from employee_info where department = %s;"
    val = (department, )
    cursor.execute(query2,val)
    records = cursor.fetchall()
    for ele in records:
        print(ele)

    print("")
    print("employee with highest salary")
    cursor.execute(query3)
    records = cursor.fetchall()
    for ele in records:
        print(ele)

    print("")
    print("employee with lowest salary")
    cursor.execute(query4)
    records = cursor.fetchall()
    for ele in records:
        print(ele)

read_emp_info()

