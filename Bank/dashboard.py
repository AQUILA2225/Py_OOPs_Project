class Dashboard:
    def __init__(self,i):
        print("Dashboard")
        print(i)
        
        while True:
            print("explore customer features - XYZ BANK ")
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Check Balance")
            print("4. Exit")
            
            
            op = int(input("Enter option: "))
            
            if op == 1:
                from dbConnection import cursorObj, conObj
                
                p = input("Enter password to withdraw the amount: ")
                amt = int(input("Enter amount to draw here:"))
                def withdraw(incomingP, withdrawAmt):
                    nonlocal i
                    
                    if incomingP == i[len(i)-1]:
                        if withdrawAmt < i[3]:
                            i=list(i)
                            i[3]-=withdrawAmt
                            return i[3]
                        else:
                            print(f"insufficient funds: your balance is {i[3]}")
                            return "insufficient funds"
                    else:
                        print("wrong pin ")
                rem_bal = withdraw(p,amt)
                q="update users set balance=%s where acc_num=%s and password=%s"
                d=(rem_bal,i[2],p)
                cursorObj.execute(q,d)
                conObj.commit()
                print(f"remaining balance is {rem_bal} and withdrawn amount is {amt}")
                        
            elif op ==2:
                from dbConnection import cursorObj, conObj
                
                p = input("Enter password to deposite amount: ")
                d_amt = int(input("Enter amount to deposite: "))
                
                def deposite(incomingP, depositeAmt):
                    nonlocal i
                    if incomingP == i[len(i)-1]:
                        if depositeAmt > 0:
                            i = list(i)
                            i[3]+=depositeAmt
                            return i[3]
                        else:
                                print("Deposit amount should be greater than 0")
                                
                    else:
                            print("Wrong pin")
                        
                total_bal = deposite(p,d_amt)
                if total_bal is not None:
                    query = "update users set balance=%s where acc_num=%s and password=%s"
                    data = (total_bal, i[2],p)
                    cursorObj.execute(query, data)
                    conObj.commit()
                    print(f"Total balance is {total_bal} and deposited amount is {d_amt}") 
                
            elif op == 3:
                p = input("Enter password to check the balance")
                def check_bal(incomingP):
                    if incomingP == i[len(i)-1]:
                        return i[3]
                    else:
                        print("Enter proper pin to proceed further")
                    
                bal = check_bal(p)
                print(f"main bal is {bal}")
                
            elif op == 4:
                break
            