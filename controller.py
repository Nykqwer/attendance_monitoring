from mysql.connector import connect, Error


connection = None

try:
    connection = connect(
        host="localhost",
        user="root",
        password="",
        database="attendance_monitoring",
        port="3308"
    )
    
    cursor = connection.cursor()
    print("Connected to the database!")
    
    
    def checkUser(username, password=None):
        cmd = f"Select count(username) from user where username='{username}' and BINARY password='{password}'"
        cursor.execute(cmd)
        cmd = None
        a = cursor.fetchone()[0] >= 1
        return a
    
    
    def add_section(blk,no_students, no_present, no_absent, no_late):
        try:
            query = "INSERT INTO block(blk,no_students, no_present, no_absent, no_late) VALUES (%s, %s, %s, %s, %s)"
            values = (blk,no_students, no_present, no_absent, no_late)
            cursor.execute(query, values)
            connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        
    def get_total_amount_student():
         try:
            cmd = """SELECT SUM(no_students) FROM block;"""
            cursor.execute(cmd)
            total_amount = cursor.fetchone()[0]
            
            if total_amount is None:
                total_amount = 0
            return total_amount
            
         except Exception as e:
            print(f"Error: {e}")
            return []
    def get_total_amount_present():
         try:
            cmd = """SELECT SUM(no_present) FROM block;"""
            cursor.execute(cmd)
            total_amount = cursor.fetchone()[0]
            
            if total_amount is None:
                total_amount = 0
            return total_amount
            
         except Exception as e:
            print(f"Error: {e}")
            return []
    def get_total_amount_absent():
         try:
            cmd = """SELECT SUM(no_absent) FROM block;"""
            cursor.execute(cmd)
            total_amount = cursor.fetchone()[0]
            
            if total_amount is None:
                total_amount = 0
            return total_amount
            
         except Exception as e:
            print(f"Error: {e}")
            return []
        
    def get_total_amount_late():
         try:
            cmd = """SELECT SUM(no_late) FROM block;"""
            cursor.execute(cmd)
            total_amount = cursor.fetchone()[0]
            
            if total_amount is None:
                total_amount = 0
            return total_amount
            
         except Exception as e:
            print(f"Error: {e}")
            return []

    def students(no_students):
        try:
            query = "INSERT INTO total_students(totalStudents) VALUES (%s)"
            values = (no_students,)  # Ensure values are passed as a tuple
            cursor.execute(query, values)
            connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
                
    def get_section():
        try:
            cmd = "SELECT id, blk,no_students, no_present, no_absent, no_late FROM block;"
            cursor.execute(cmd)
            result = cursor.fetchall()
            print("data: ", result)

            return result
            
        except Exception as e:
            print(f"Error: {e}")
            return []



     
    def update_section(id,no_present, no_absent, no_late):
        cmd = f"update block set no_present='{no_present}',no_absent='{no_absent}', no_late ='{no_late}' where id = '{id}';"
        cursor.execute(cmd)
        connection.commit()
        if cursor.rowcount == 0:
            return False
        return True
    
    def update_section_all(id,blk,no_students,no_present, no_absent, no_late):
        cmd = f"update block set blk = '{blk}', no_students ='{no_students}', no_present='{no_present}',no_absent='{no_absent}', no_late ='{no_late}' where id = '{id}';"
        cursor.execute(cmd)
        connection.commit()
        if cursor.rowcount == 0:
            return False 
        return True
            
        
  
    def delete_section(id):
        cmd = f"delete from block where id='{id}';"
        cursor.execute(cmd)
        connection.commit() 
        if cursor.rowcount == 0:
            return False
        return True
    
except Error as e:
    print(f"Error: {e}")
    