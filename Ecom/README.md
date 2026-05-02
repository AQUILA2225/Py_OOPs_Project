# E-Commerce Order System (OOP + PDBC)

## Project Overview

This project is a console-based E-Commerce Order System developed using Python with Object-Oriented Programming concepts and MySQL for database management through Python Database Connectivity (PDBC).

The system simulates a basic online shopping workflow where users can register, log in, view products, add items to a cart, place orders, cancel orders, and view payment history.

---

## Features

* User Signup and Login
* Add Product
* View Products
* Add to Cart
* Place Order
* Cancel Order
* Payment History
* Stock Validation and Auto Update

---

## OOP Concepts Used

* Classes and Objects
* Encapsulation
* Constructors (`__init__`)
* Method-based design
* Modular programming

---

## Database Design

### Tables

#### users

* user_id (Primary Key)
* name
* email
* password

#### products

* product_id (Primary Key)
* product_name
* price
* quantity

#### orders

* order_id (Primary Key)
* user_id (Foreign Key)
* product_id (Foreign Key)
* quantity
* total_amount
* order_status
* payment_status

---

## Project Structure

```
ecommerce_order_system/
│
├── dbConnection.py
├── user.py
├── product.py
├── order.py
├── app.py
```

---

## Technologies Used

* Python
* MySQL
* mysql-connector-python

---

## How to Run

1. Install required package:

```
pip install mysql-connector-python
```

2. Create database:

```
CREATE DATABASE ecommerce_db;
```

3. Update database credentials in:

```
dbConnection.py
```

4. Run the project:

```
python app.py
```

---

## Functional Flow

```
User Login → View Products → Add to Cart → Place Order → Payment History
```

---

## Highlights

* Stock validation before placing orders
* Cart-based order processing
* Modular design using OOP
* Database integration using PDBC
* Menu-driven application

---

## Future Enhancements

* GUI using Tkinter or Web interface using Flask/Django
* Payment gateway integration
* Admin panel
* Order tracking system
* Cart table in database

---

## Author

Bharathi

---

## Conclusion

This project demonstrates practical implementation of OOP concepts with database connectivity. It reflects real-world application flow and serves as a strong foundation for building scalable systems.
