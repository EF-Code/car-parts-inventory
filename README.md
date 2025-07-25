
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
### Dashboard
<img width="1900" height="984" alt="Screenshot From 2025-07-25 00-39-57" src="https://github.com/user-attachments/assets/6a56d5cb-b461-4efb-825a-42c7cb1274c3" />

### Add Part
<img width="1901" height="1043" alt="Screenshot From 2025-07-25 00-40-39" src="https://github.com/user-attachments/assets/0b17417c-6167-4fce-a301-0219401936fe" />

### View Inventory
<img width="1901" height="1043" alt="Screenshot From 2025-07-25 00-40-50" src="https://github.com/user-attachments/assets/8b879706-8329-488c-9635-9972a174c422" />

### Update Inventory
<img width="1901" height="1043" alt="Screenshot From 2025-07-25 00-41-00" src="https://github.com/user-attachments/assets/46a41d93-c50e-4add-8753-b077e2f2553e" />

### Delete Parts

<img width="1901" height="1043" alt="Screenshot From 2025-07-25 00-41-08" src="https://github.com/user-attachments/assets/c5aa7dbe-2a61-4cb0-a6e5-008f88767202" />



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
| [Suleiman](https://github.com/suleiman108) | Edited README            |

