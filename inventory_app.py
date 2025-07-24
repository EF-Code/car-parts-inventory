from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'inventory_db'

mysql = MySQL(app)

@app.route('/')
def dashboard():
    cur = mysql.connection.cursor()
    cur.execute("SELECT COUNT(*) FROM items")
    total_items = cur.fetchone()[0]

    cur.execute("SELECT * FROM items WHERE quantity < 5")
    low_stock = cur.fetchall()

    cur.execute("SELECT * FROM items ORDER BY id DESC LIMIT 5")
    recent = cur.fetchall()
    cur.close()
    return render_template('dashboard.html', total=total_items, low_stock=low_stock, recent=recent)
