import dbconn

def delete_emp_info(empid):
    conn = dbconn.get_connection()
    query = f"delete from employee_info where empid = %s;"
    val = (empid, )

    cursor = conn.cursor()
    cursor.execute(query, val)
    conn.commit()
    cursor.close()
    conn.close()



delete_emp_info(4)