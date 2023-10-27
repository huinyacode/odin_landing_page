import mysql.connector

db = mysql.connector.connect(
    port="3305",
    host="localhost",
    user="root",
    passwd="zxclown",
    auth_plugin='mysql_native_password',
    database="gosling_database"
)
mycursor = db.cursor()

# mycursor.execute("CREATE TABLE test_results (name VARCHAR(50), result VARCHAR(100), PresoID int PRIMARY KEY AUTO_INCREMENT)")
# mycursor.execute("INSERT INTO test_results (name, result) VALUES (%s,%s)", ('nik', 'horny_gosling') )
# db.commit()

mycursor.execute("SELECT * FROM test_results")

for x in mycursor:
    print(x)