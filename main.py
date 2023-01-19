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

    # def deleteMachine():
    #     # TODO: delete vending machine.
    #
    # def editMachine():
    #     # TODO: edit name, location of vending machine.
    #
    # def addProduct():
    #     # TODO: There are multiple products like coke, taro, sprite.
    #
    # def editProduct():
    #     # TODO: edit the amount of product.
    #
    # def removeProduct():
    #     # TODO: remove product from the vending machine.
    #
    def listing(self):
        conn = self.generate_conn_singleton()
        cursor = conn.cursor()
        cursor.execute('select * from machine_info')
        data = cursor.fetchall()
        return data


ans = VendingMachine()
ans.createMachine("Machine_prototype", "MUIC")
print(ans.listing())
