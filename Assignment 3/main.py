import psycopg2
from psycopg2 import sql

# Function to establish connection to PostgreSQL database
def connect_to_db():
    try:
        connection = psycopg2.connect(
            dbname="students",
            user="postgres",
            password="fast",  # Replace with your PostgreSQL password
            host="localhost",
            port="5432"
        )
        print("Connected to PostgreSQL database!")
        return connection
    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL database:", e)
        return None

# Function to retrieve all students from the database
def getAllStudents(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students;")
        students = cursor.fetchall()
        cursor.close()
        return students
    except psycopg2.Error as e:
        print("Error retrieving students:", e)
        return []

# Function to add a new student to the database
def addStudent(connection, first_name, last_name, email, enrollment_date):
    try:
        cursor = connection.cursor()
        insert_query = sql.SQL("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);")
        cursor.execute(insert_query, (first_name, last_name, email, enrollment_date))
        connection.commit()
        cursor.close()
        print("Student added successfully!")
    except psycopg2.Error as e:
        print("Error adding student:", e)

# Function to update email address of a student
def updateStudentEmail(connection, student_id, new_email):
    try:
        cursor = connection.cursor()
        update_query = sql.SQL("UPDATE students SET email = %s WHERE student_id = %s;")
        cursor.execute(update_query, (new_email, student_id))
        connection.commit()
        cursor.close()
        print("Email address updated successfully!")
    except psycopg2.Error as e:
        print("Error updating email address:", e)

# Function to delete a student from the database
def deleteStudent(connection, student_id):
    try:
        cursor = connection.cursor()
        delete_query = sql.SQL("DELETE FROM students WHERE student_id = %s;")
        cursor.execute(delete_query, (student_id,))
        connection.commit()
        cursor.close()
        print("Student deleted successfully!")
    except psycopg2.Error as e:
        print("Error deleting student:", e)

# Main function
def main():
    # Connect to the database
    connection = connect_to_db()
    if connection is None:
        return

    # Test functions
    print("Testing getAllStudents:")
    print(getAllStudents(connection))

    print("\nTesting addStudent:")
    #lets add a student
    # addStudent(connection, "Alice", "Johnson", "alice.johnson@example.com", "2024-03-18")


    print("\nTesting updateStudentEmail:")
    # updateStudentEmail(connection, 1, "john.doe@example.org")

    print("\nTesting deleteStudent:")
    deleteStudent(connection, 2)

    # Close connection
    connection.close()
    print("Disconnected from PostgreSQL database!")

if __name__ == "__main__":
    main()
