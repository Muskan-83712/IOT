import dbconn


def update_emp_info(empid,salary):
    conn = dbconn.get_connection()
    query = f"update employee_info SET salary = %s where empid = %s;"
    val = (salary, empid)
    cursor = conn.cursor()
    cursor.execute(query, val)
    conn.commit()
    cursor.close()
    conn.close()

update_emp_info(3,70000)