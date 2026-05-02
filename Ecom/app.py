from user import User
from product import Product
from orders import Orders

current_user_id = None
cart = []

while True:
    print("\n E-Commerce Order System")
    print("1.Signup")
    print("2. Login")
    print("3. Add Product")
    print("4. View Products")
    print("5. Add to Cart")
    print("6. Place Order")
    print("7. Cancel Order")
    print("8. Payment History")
    print("9. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
    
        us = User(name, email, password)
        us.signup()
        
    elif choice == 2:
        email = input("Enter you email: ")
        password = input("Enter your password: ")

        us = User(email = email, password = password)
        logged_user = us.login()
        
        if logged_user:
            current_user_id = logged_user[0]
            print("Current logged in user",current_user_id)
        
    elif choice == 3:
        pro_name = input("Enter Product Name: ")
        pro_price = float(input("Enter Price: "))
        qnty = int(input("Enter quantity: "))

        pro = Product(pro_name, pro_price, qnty)
        pro.add_product()
        
    elif choice == 4:
        pro1=Product()
        pro1.view_products()
        
    elif choice == 5:
        if current_user_id is None:
            print("Please Login first")
        else:
            pro = Product()
            pro.view_products()
            
            # cart=[]
            product_id = int(input("Enter product id to add to cart: "))
            product_name = input("Enter Name of the product: ")
            quantity = int(input("Enter quantity: "))

            cart.append({
                "product_id": product_id,
                "product_name": product_name,
                "quantity": quantity
                })

            print("Product added to cart successfully")
            print("Current cart:", cart)
    
    elif choice == 6:
        if current_user_id is None:
            print("Please login first")
            
        elif len(cart) == 0: # checks if cart has products or not
            print("Cart is empty. Please add products first")
        else:
            all_orders_placed = True
            
            for item in cart: 
                product_id = item["product_id"]
                product_name = item["product_name"]
                quantity = item["quantity"]
                
                # user_id = int(input("Enter user ID: "))
                # product_id = int(input("Enter product ID: "))
                # quantity = int(input("Enter quantity: "))

                o = Orders(current_user_id, product_id, product_name, quantity)
                result = o.place_order()
                
                if result == False:
                    all_orders_placed = False
            
            if all_orders_placed:
                cart.clear()
                print("Cart cleared after placing order")
            else:
                print("Some orders failed. Cart is not cleared")
        
    elif choice == 7:
        order_id = int(input("Enter order ID to cancel: "))

        o = Orders()
        o.cancel_order(order_id)
        
    elif choice == 8:
        user_id = int(input("Enter user ID: "))

        o = Orders(user_id=user_id)
        o.payment_history()
    
    elif choice == 9:
        print("Thank you for using E-Commerce Order System")
        break
    
    else:
        print("Invalid choice")




