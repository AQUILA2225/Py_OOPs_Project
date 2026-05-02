class Dashboard:
    def __init__(self, loggedInUser):
        print("Welcome to XYZ Bank")
        print(f"welcome {loggedInUser} to XYZ Bank")
        
while True:
    print("1. Register")
    print("2. Login")
    
    op = int(input("Enter option: "))
    
    if op ==1:
        from register import Register
        
    elif op == 2:
        from login import Login
    

        
        
