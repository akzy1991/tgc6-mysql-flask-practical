from data import get_conn, get_cursor
import os

conn = get_conn("localhost",
                os.environ.get("DB_USER"),
                os.environ.get("DB_PASSWORD"),
<<<<<<< HEAD
                "Chinook")
=======
                "Chinook"
                )
>>>>>>> ba5acc2aa03455d8ae00eccb6315446e411f0a31

cursor = get_cursor(conn)

while True:
    print("Select what to search by:")
<<<<<<< HEAD
    print("1. Track Name")
    print("2. Composer Name")
=======
    print("1. Track name")
    print("2. Composer name")
>>>>>>> ba5acc2aa03455d8ae00eccb6315446e411f0a31
    print("3. Quit")

    choice = input("Enter your choice: ")
    sql = ""

    if choice == "1":
        track_name = input("Please enter a track name: ")

        sql = f"""
<<<<<<< HEAD
        SELECT * FROM Track where Name LIKE "%{track_name}%"
        LIMIT 10
=======
        select * from Track where Name like "%{track_name}%"
        limit 10
>>>>>>> ba5acc2aa03455d8ae00eccb6315446e411f0a31
        """
    elif choice == "2":
        composer_name = input("Please enter the composer name: ")

        sql = f"""
<<<<<<< HEAD
        SELECT * FROM Track where Composer LIKE "%{composer_name}%"
        LIMIT 10
        """

    elif choice == "3":
        break

    
=======
        select * from Track where Composer like "%{composer_name}%"
        """

        print(sql)

    elif choice == "3":
        break

    cursor.execute(sql)

    print("Search Results")
    for each_result in cursor:
        print("Track Name:", each_result["Name"])
        print("Composers", each_result["Composer"])
>>>>>>> ba5acc2aa03455d8ae00eccb6315446e411f0a31
