import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="mysql"
)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Create a table if it doesn't exist
create_table_query = """
    CREATE TABLE IF NOT EXISTS employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        age INT,
        department VARCHAR(255)
    )
"""
cursor.execute(create_table_query)

# Insert data into the table
insert_query = """
    INSERT INTO employees (name, age, department)
    VALUES (%s, %s, %s)
"""
employee_data = [
    ("John Doe", 30, "Sales"),
    ("Jane Smith", 35, "Marketing"),
    ("Bob Johnson", 28, "IT")
]

cursor.executemany(insert_query, employee_data)
db.commit()

# Fetch and display all records
select_query = "SELECT * FROM employees"
cursor.execute(select_query)
employees = cursor.fetchall()

for employee in employees:
    print(f"ID: {employee[0]}, Name: {employee[1]}, Age: {employee[2]}, Department: {employee[3]}")

# Close the database connection
db.close()

