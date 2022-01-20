from distutils.log import debug
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_HOST'] = 'crud_db'
app.config['MYSQ_PORT'] = 3306
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL()
mysql.init_app(app)


@app.route('/', methods=['POST', 'GET'])
def index():
    cursor = mysql.connection.cursor()
    cursor.execute(f"use newsstand_db;")
    cursor.execute(f"SELECT np. *, ed. * FROM newspapers as np, editors as ed where np.ed_id = ed.ed_id;")
    np_list = cursor.fetchall()
    cursor.close()

    return render_template("index.html", len = len(np_list), np_list = np_list)


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        cursor = mysql.connection.cursor()
        cursor.execute(f"use newsstand_db;")
        np_name = request.form['np_name']
        np_url = request.form['np_url']
        ed_firstname = request.form['ed_firstname']
        ed_lastname = request.form['ed_lastname']
        ed_datestarted = request.form['ed_datestarted']

        cursor.execute(f"INSERT INTO `newspapers` (`np_name`, `np_url`) VALUES ('{np_name}','{np_url}');")
        mysql.connection.commit()
        cursor.execute(f"INSERT INTO `editors` (`ed_firstname`, `ed_lastname`, `ed_datestarted`) VALUES ('{ed_firstname}','{ed_lastname}','{ed_datestarted}');")
        mysql.connection.commit()                                            
        cursor.close()
        return render_template("add.html")
    return render_template("add.html")


@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        cursor = mysql.connection.cursor()
        cursor.execute(f"use newsstand_db;")
        #np_name = request.form['np_name']
        ed_firstname = request.form['ed_firstname']
        ed_lastname = request.form['ed_lastname']
        ed_datestarted = request.form['ed_datestarted']

        cursor.execute(f"UPDATE `editors` SET `ed_datestarted`='{ed_datestarted}' WHERE `ed_firstname`='{ed_firstname}' AND `ed_lastname`='{ed_lastname}';")
        mysql.connection.commit()
        cursor.close()
        return render_template("add.html")
    return render_template("update.html")


@app.route('/delete', methods=['POST', 'GET'])
def delete():
    if request.method == 'POST':
        cursor = mysql.connection.cursor()
        cursor.execute(f"use newsstand_db;")
        ed_firstname = request.form['ed_firstname']
        ed_lastname = request.form['ed_lastname']

        cursor.execute(f"DELETE FROM `editors` WHERE `ed_firstname`='{ed_firstname}' AND `ed_lastname`='{ed_lastname}';")
        mysql.connection.commit()
        cursor.close
        return render_template("update.html")
    return render_template("delete.html")



@app.route("/help")
def help():
    return render_template("help.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",  debug=True)


