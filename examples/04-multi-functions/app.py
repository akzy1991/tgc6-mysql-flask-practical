from data import get_conn, get_cursor
import os

conn = get_conn("localhost",
                os.environ.get("DB_USER"),
                os.environ.get("DB_PASSWORD"),
                "Chinook")

cursor = get_cursor(conn)

while True:
    print("Select what to search by:")
    print("1. Track Name")
    print("2. Composer Name")
    print("3. Quit")

    choice = input("Enter your choice: ")
    sql = ""

    if choice == "1":
        track_name = input("Please enter a track name: ")

        sql = f"""
        SELECT * FROM Track where Name LIKE "%{track_name}%"
        LIMIT 10
        """
    elif choice == "2":
        composer_name = input("Please enter the composer name: ")

        sql = f"""
        SELECT * FROM Track where Composer LIKE "%{composer_name}%"
        LIMIT 10
        """

    elif choice == "3":
        break

    
