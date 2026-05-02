from dbConnection import dbcon, cursorObj

class Orders:
    def __init__(self,user_id=None,product_id=None,quantity=None):
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity
        
    def place_order(self):
        query = "SELECT price,quantity FROM products WHERE product_id = %s"
        cursorObj.execute(query, (self.product_id,))
        result = cursorObj.fetchone()
        
        if result:
            price = result[0]
            available_quantity = result[1]
            
            if self.quantity > available_quantity:
                print("Not enough stock available")
                print("Available quantity:", available_quantity)
            else:
                total_amount = price * self.quantity
            
                query = """
                    INSERT INTO orders(user_id, product_id, quantity, total_amount, order_status, payment_status)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """
                data = (self.user_id, self.product_id, self.quantity, total_amount, "Placed", "Paid")
            
                cursorObj.execute(query, data)
                dbcon.commit()
            
                print("Order placed successfully")
                print("Total Amount:", total_amount)
        else:
            print("Invalid product ID")
            
    def cancel_order(self, order_id):
        query = "update orders set order_status = %s where order_id = %s"
        data = ("Cancelled", order_id)
        
        cursorObj.execute(query,data)
        dbcon.commit()
        
        if cursorObj.rowcount>0:
            print("Order cancelled successfully")
        else:
            print("Invalid order ID")
            
    def payment_history(self):
        query = "SELECT * FROM orders WHERE user_id = %s"
        cursorObj.execute(query, (self.user_id,))
        orders = cursorObj.fetchall()

        if orders:
            print("\nPayment History")
            print("---------------------")

            for order in orders:
                print("Order ID:", order[0])
                print("User ID:", order[1])
                print("Product ID:", order[2])
                print("Quantity:", order[3])
                print("Total Amount:", order[4])
                print("Order Status:", order[5])
                print("Payment Status:", order[6])
                print("---------------------")
        else:
            print("No orders found")
            