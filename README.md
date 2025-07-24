
# Inventory Management System

A simple web-based Inventory Management System built using **Flask**, and **MySQL**, designed specifically for managing car parts. It contains the Crud features; Create item, Read item, Update item and Delete item as Add item, View inventory, Update item and Delete item.

---

## 📦 Features

- ✅ **Dashboard** showing total parts, low stock alerts, and recent additions.
- ➕ **Add Car Part** with material, quantity, and pricing info.
- 📋 **View Inventory** with search functionality.
- ✏️ **Edit Existing Parts**
- 🗑️ **Delete Car Parts**
- 🔍 **Filter and Update Inventory**

---

## 🖼️ Screenshots




## 💻 Technologies Used

- **Python 3**
- **Flask**
- **MySQL**
- **Flask-MySQLdb**

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ef-code/flask-grud.git
cd flask-crud
````

### 2. Set Up MySQL Database

Open MySQL and run:

```sql
CREATE DATABASE inventory_db;

USE inventory_db;

CREATE TABLE items (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  material VARCHAR(100),
  quantity INT,
  sales_price DECIMAL(10, 2),
  purchase_price DECIMAL(10, 2)
);
```

### 3. Create a Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### 4. Run the App

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---


## 👥 Contributors


| Name                                       | Contributions                                                                                                 |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------|
| [Emmanuel](https://github.com/EF-Code)     | Created dashboard, add_item function and inventory database                                                   |
| [Gidado](https://github.com/gidadojnr)     | Created view_inventory and edit_item functions                                                                |
| [Apochi](https://github.com/emm847)        | Created delete parts                                                                                          |
| [Henry](https://github.com/kingdavida001)  | Created update_list and delete_item                                                                           |


