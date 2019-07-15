import pymysql

# Create a connection object

dbServerName    = "172.17.0.2"
dbUser          = "root"
dbPassword      = "darrensmells"
dbName          = "testdb"
charSet         = "utf8mb4"

connectionObject   = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,
                                     db=dbName, charset=charSet)

try:                                
    # Create a cursor object
    cursorObject            = connectionObject.cursor()                                    
    # SQL string to create a MySQL table
    sqlCreateTableCommand   = "CREATE TABLE Employee(id int, LastName varchar(32), FirstName varchar(32), DepartmentCode int)"
    # Execute the sqlQuery
    cursorObject.execute(sqlCreateTableCommand)
    # List the tables using SQL command
    sqlShowTablesCommand    = "show tables"   
    # Execute the SQL command
    cursorObject.execute(sqlShowTablesCommand)
    #Fetch all the rows - from the command output
    rows                = cursorObject.fetchall()

    for row in rows:
        print(row)

    # Insert rows into the MySQL Table
    insertStatement = "INSERT INTO Employee (id, LastName, FirstName, DepartmentCode) VALUES (1,'Albert','Einstein',10)"  
    cursorObject.execute(insertStatement)

    # SQL Query to retrive the rows
    sqlQuery    = "select * from Employee"   

    #Fetch all the rows - for the SQL Query
    cursorObject.execute(sqlQuery)
    rows = cursorObject.fetchall()

    for row in rows:
        print(row)

except Exception as e:
    print("Exeception occured:{}".format(e))

finally:
    connectionObject.close()