from dbConnection import cursorObj,conObj

class Login:
    def __init__(self, an, p): 
        queryToFetchData = "select * from users"
        cursorObj.execute(queryToFetchData)
        userData = cursorObj.fetchall()
        
        for i in userData:
            if i[2] == an and i[4] == p:
                from dashboard import Dashboard
                Dashboard(i)
                break
            else:
                print("customer not found with that details")
                continue
        
        
        print("login class")
        

acc = input("Enter account number:")
pwd = input("Enter password: ")
Login(acc,pwd)
