import sqlite3

class DBManager:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('inventorydb.db')
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print("Failed connecting to database...")

    def create_table(self, tableName, tableColumn):
        conn = self.cursor
        conn.execute("CREATE TABLE if not exists {0}({1});".format(tableName,tableColumn))

    def addData(self, tableName, newData):
        conn = self.cursor
        conn.execute("INSERT INTO {0} VALUES ({1});" .format(tableName, newData))
        self.conn.commit()

    def updateData(self, tableName, newValue, condition):
        conn = self.cursor
        conn.execute("UPDATE {0} SET {1} WHERE {2};".format(tableName,newValue,condition))
        self.conn.commit()

    def deleteData(self, tablename, condition):
        conn = self.cursor
        conn.execute("DELETE FROM {0} WHERE {1};".format(tablename,condition))
        self.conn.commit()
        
    def showData(self, tableName):
        conn = self.cursor
        conn.execute("SELECT * FROM {0};".format(tableName))
        return conn.fetchall()
        
    def showDataLimited(self,column,tableName):
        conn = self.cursor
        conn.execute("SELECT {0} FROM {1};".format(column, tableName))
        return conn.fetchall()

    def showDataSpecific(self, function, tableName, condition):
        conn = self.cursor
        conn.execute("SELECT {0} FROM {1} {2};".format(function, tableName,condition))
        return conn.fetchall()
