from flask import Flask, request, render_template, Response
import mysql.connector
import json

#from flask_mysqldb import MySQL

app = Flask(__name__)

#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'root'
#app.config['MYSQL_DB'] = 'PeopleDB'
#port, intet password, intet user
def connection():
    return mysql.connector.connect(user='root', host='database', port='3306', password='',database='PeopleDB')


@app.route('/test', methods=['POST'])
def test():
    return "success"

@app.route('/peopleDB', methods=['GET', 'POST'])
def index():
    conn = connection()

    if request.method == "POST":
        details = request.form
        firstName = details['firstname']
        lastName = details['lastname']
        cur = conn.cursor()
        cur.execute("INSERT INTO PeopleTable(Firstname, Lastname) VALUES (%s, %s)", (firstName, lastName))
        conn.commit()
        #mysql.connection.commit()
        cur.close()
        conn.close()
        return 'success'
    #return render_template('index.html')

    if request.method == "GET":
        cur = conn.cursor()
        cur.execute("SELECT PersonID, Firstname, Lastname FROM PeopleTable")
        row = [x[0] for x in cur.description]
        r = cur.fetchall()
        json_data = []
        for result in r:
            json_data.append(dict(zip(row, result)))
        cur.close()
        conn.close()
        return json.dumps(json_data)
        #string = ''
        #cur = conn.cursor()
        #cur.execute("SELECT Firstname, Lastname FROM PeopleTable")
        #for row in cur.fetchall():
        #    string += row[0] + ', '
        #cur.close()
        #return string

# This statement evaluates to true if this is the main python file. It starts up the Flask app on localhost with the default port 5000.
if __name__ == '__main__':
    app.run(host='0.0.0.0')