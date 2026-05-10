import mysql.connector
from mysql.connector import errorcode

"""
Function from mysql.connector that establishes the connection using connection_info dictionary
"""
def open_connection(connection_info):
    # This code for this try/except block was gotten from the official MySQL documentation: 
    # https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
    try:
        cnx = mysql.connector.connect(**connection_info)
        return cnx
    except mysql.connector.Error as err:
        if(err.errno == errorcode.ER_ACCESS_DENIED_ERROR):
            print("There is an issue with your username or password.")
            return None
        elif(err.errno == errorcode.ER_BAD_DB_ERROR):
            print("The database you're trying to access doesn't exist.")
            return None
        else:
            print(err)
            return None

"""
This function closes the cursor used to access the database and closes the connection to the database.
"""
def close_connection(cnx, executor):
    executor.close()
    cnx.close()