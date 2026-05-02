from dbConnection import dbcon, cursorObj

class Product:
    def __init__(self, product_name=None, price=None,quantity=None):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
    
    def add_product(self):
        query = "insert into products(product_name, price, quantity) values (%s, %s, %s)"
        data = (self.product_name, self.price, self.quantity)
        
        cursorObj.execute(query, data)
        dbcon.commit()
        
        print("Product added successfully!!")
        
    def view_products(self):
        query = "select * from products"
        cursorObj.execute(query)
        products = cursorObj.fetchall()
        
        if products:
            print("Available Products")
            print("----------------------")
            
            for product in products:
                print("Product ID:", product[0])
                print("Product Name:", product[1])
                print("Price:", product[2])
                print("Quantity:", product[3])
                print("----------------------")
                # print(products)
                
        else:
            print("No products available")