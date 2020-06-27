from data import get_conn, get_cursor
from flask import Flask, render_template, request, redirect, url_for
import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

conn = get_conn("localhost",
                os.environ.get("DB_USER"),
                os.environ.get("DB_PASSWORD"),
                "Chinook"
                )

cursor = get_cursor(conn)

app = Flask(__name__)

@app.route('/genre/create')
def show_create_artist_form():
    return render_template('create_genre.template.html')


# @app.route('/genre/create', methods=["POST"])
# def process_create_artist():
#     genre_name = request.form.get("genre_name")

#     sql = f"""
#     insert into Genre (Name) values ("{genre_name}");
#     """

#     cursor.execute(sql)


#     # Whenever we change the database, we have to remember to COMMIT
#     # the transactions
#     conn.commit()

#     return "genre added"



# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
