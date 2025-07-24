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

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        material = request.form['material']
        quantity = request.form['quantity']
        sales_price = request.form['sales_price']
        purchase_price = request.form['purchase_price']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO items (name, material, quantity, sales_price, purchase_price) VALUES (%s, %s, %s, %s, %s)",
                    (name, material, quantity, sales_price, purchase_price))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('view_inventory'))
    return render_template('add_item.html')
