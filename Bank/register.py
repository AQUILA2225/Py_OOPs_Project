from dbConnection import cursorObj, conObj

class Register:
    def __init__(self, n, a, fst_bal): # these values are sent to user table of bankdb
        queryTableCreation="""
        create table if not exists users(
            customer_id int primary key auto_increment,
            name varchar(50) not null unique,
            acc_num varchar(16) not null,
            balance decimal(10,2) not null,
            password varchar(16) not null
        )
        """
        cursorObj.execute(queryTableCreation)
        p = input("Enter password here:")
        c_p = input("Enter password again to confirm:")
        if p==c_p:
            query = "insert into users(name,acc_num,balance,password) values (%s,%s,%s,%s)"
            data = (n,a,fst_bal,p)
            cursorObj.execute(query,data)
            conObj.commit()
            print("user registered successfully")
        else:
            print("Invalid credentials")
            
            if True:
                from login import Login
                accNum_input_Login = input("Enter your account number:")
                p_Login=input("Enter password here:")
                Login(accNum_input_Login, p_Login)
                

name_input = input("Enter your Name:")
acc_num_input = int(input("Enter your Account Number:"))
first_balance = int(input("Enter your balance:"))
obj = Register(name_input, acc_num_input, first_balance)