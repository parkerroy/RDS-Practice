import pymysql

#Configuration Values
endpoint = 'aws-practice.cbc577lypslk.us-east-1.rds.amazonaws.com'
username = 'admin'
password = '<ENTER PASSWORD>'
database_name = 'Transactions_Prod'

#Connections
connection = pymysql.connect(endpoint, user=username, passwd=password, db=database_name)



def lambda_handler(event, context):
    cursor = connection.cursor()
    cursor.execute('SELECT * from Transactions')

    row = cursor.fetchall()

    for row in rows:
        print("{0} {1} {2}".format(row[0], row[1], row[2]))
