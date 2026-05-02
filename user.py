from dbConnection import dbcon, cursorObj

class User:
    def __init__(self, name = None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password
        
    def signup(self):
        query = "insert into users (name,email,password) values (%s, %s, %s)"
        data = (self.name,self.email,self.password)
        cursorObj.execute(query, data)
        dbcon.commit()
        print("User registered successfully")
        
    def login(self):
        query = "select * from users where email =%s and password = %s"
        data = (self.email, self.password)
        
        cursorObj.execute(query, data)
        result = cursorObj.fetchone()
        
        if result:
            print("Login Successful")
            return result
        else:
            print("Invalid email or password")
            return None
        
        