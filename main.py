import mysql.connector


class VendingMachine:
    def __init__(self):
        super().__init__()

    def generate_conn_singleton(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="vending_machine"
        )
        return conn

    # creating machine
    def createMachine(self, mach_name, mach_location):
        conn = self.generate_conn_singleton()
        cursor = conn.cursor()
        sql = """INSERT INTO machine_info(
        machine_name, location)
        VALUES (%s,%s)"""
        data = (mach_name, mach_location)
        try:
            # Executing the SQL command
            cursor.execute(sql, data)

            # Commit your changes in the database
            conn.commit()

        except:
            # Rolling back in case of error
            conn.rollback()

        # Closing the connection
        conn.close()

    def deleteMachine(self, mach_id):
        conn = self.generate_conn_singleton()
        cursor = conn.cursor()
        sql = """DELETE FROM machine_info WHERE id = %s"""
        try:
            # Executing the SQL command
            cursor.execute(sql, mach_id)

            # Commit your changes in the database
            conn.commit()

        except:
            # Rolling back in case of error
            conn.rollback()

        # Closing the connection
        conn.close()

    def editMachine(self, mach_id, updated_name, updated_location):
        conn = self.generate_conn_singleton()
        cursor = conn.cursor()

        sql = """UPDATE machine_info SET machine_name = %s  WHERE id = %s"""
        data = (updated_name, mach_id)
        cursor.execute(sql, data)
        sql = """UPDATE machine_info SET location = %s  WHERE id = %s"""
        data = (updated_location, mach_id)
        cursor.execute(sql, data)

        # Commit your changes in the database
        conn.commit()
        conn.close()

    def addProduct(self, prod_name, prod_amount):
        conn = self.generate_conn_singleton()
        cursor = conn.cursor()
        sql = """INSERT INTO Product(
                product_name, product_amount)
                VALUES (%s,%s)"""
        data = (prod_name, prod_amount)
        try:
            # Executing the SQL command
            cursor.execute(sql, data)

            # Commit your changes in the database
            conn.commit()
        except:
            # Rolling back in case of error
            conn.rollback()

            # Closing the connection
        conn.close()

    def editProduct(self, prod_id, prod_amount, prod_bind):
        conn = self.generate_conn_singleton()
        cursor = conn.cursor()

        sql = """UPDATE machine_info SET product_amount = %s  WHERE id = %s"""
        data = (prod_amount, prod_id)
        cursor.execute(sql, data)
        sql = """UPDATE machine_info SET bind_with = %s  WHERE id = %s"""
        data = (prod_bind, prod_id)
        cursor.execute(sql, data)
        # Commit your changes in the database
        conn.commit()
        conn.close()

    def removeProduct(self, prod_id):
        conn = self.generate_conn_singleton()
        cursor = conn.cursor()
        sql = """DELETE FROM Product WHERE id = %s"""
        try:
            # Executing the SQL command
            cursor.execute(sql, prod_id)

            # Commit your changes in the database
            conn.commit()

        except:
            # Rolling back in case of error
            conn.rollback()

        # Closing the connection
        conn.close()

    def listing(self):
        conn = self.generate_conn_singleton()
        cursor = conn.cursor()
        cursor.execute('select * from machine_info')
        data = cursor.fetchall()
        return data


ans = VendingMachine()
ans.createMachine("Machine_prototype", "MUIC")
ans.editMachine("6", "second_one", "MU")
print(ans.listing())
