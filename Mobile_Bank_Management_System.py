
print("\t\t\t\t\t----------------------------------------------------------------")
print("\t\t\t\t\t|\tProject Name : Mobile Banking Management System\t\t|")
print("\t\t\t\t\t----------------------------------------------------------------")
# ----------------------------------------------------------------------------------------------
def pay_bill(balance):
    print("Payment List: ")
    print("""
                    1.Educational Institute 
                    2.Electricity 
                    3.Gas 
                    4.Internet
                    5.Water
                    
                """)

    option=int(input("Select payment option : "))

    if option==1:

        education = ["IMA","NDCM","DIU","DU"]

        a = input("Search your Educational Institute: ")
        for i in range(0,4):
            if a == education[i]:
                count=1
                break
            else:
                count=0



        if count==1:
            print("We find your Educational Institute.")
            id=input("Enter your ID:")
            payment_number=input("Enter your contact number : ")
            payment=int(input("Enter payment amount :"))
            if payment<= balance:
                print(f"""
                Payment {payment} is successful. 
                Your ID is {id}
                Your contact number is 0{payment_number}            
                """)
            else:

                payment=0

                print("""
                You have not enough money.
                Payment is not possible.
                
                
                """)

        else:
            payment = 0
            print("We not find your Educational Institute.")




    elif option==2 :

        meter = input("Enter meter number : ")
        payment = int(input("Enter amount : "))
        payment_number = input("Enter contuct number : ")



        if payment <= balance:
            print(f"""
            Payment {payment} is successful. 
            Your Meter  ID is {meter}
            Your contact number is 0{payment_number}            
            """)
        else:

            payment = 0

            print("""
            You have not enough money.
            Payment is not possible.


            """)

    elif option==3 :
        num = int(input("Enter payment number : "))
        payment = int(input("Enter amount : "))
        payment_number = input("Enter contact number :")


        if payment <= balance:
            print(f"""
            Payment {payment} is successful. 
            
            Your contact number is 0{payment_number}            
            """)
        else:

            payment = 0

            print("""
            You have not enough money.
            Payment is not possible.


            """)

    elif option == 4 :
        num = int(input("Enter payment number : "))
        payment = int(input("Enter amount : "))
        payment_number = input("Enter contact number :")

        if payment <= balance:
            print(f"""
                    Payment {payment} is successful. 

                    Your contact number is 0{payment_number}            
                    """)
        else:

            payment = 0

            print("""
            You have not enough money.
            Payment is not possible.


            """)

    elif option == 5 :

        num = int(input("Enter payment number : "))
        payment = int(input("Enter amount : "))
        payment_number = input("Enter contuct number : ")

        if payment <= balance:
            print(f"""
                    Payment {payment} is successful. 

                    Your contact number is 0{payment_number}            
                    """)
        else:

            payment = 0

            print("""
            You have not enough money.
            Payment is not possible.


            """)






    b = balance - payment


    Yes_No()
    response = int(input("Enter your choice : "))
    if response == 1:
        run()
        return b

    if response==2:
        exit()



    else:
        print("Mobile Recharge is not possible.")
        Yes_No()
        response = int(input("Enter your choice : "))
        if response == 1:
            run()




        else:
            exit()


# -------------------------------------------------------------------------------------





def run():

    print("""
                      1.Balance                     
                      2.Cash out
                      3.Send money
                      4.Mobile Recharge
                      5.Pay Bill
                      6.Payment                
                      7.Exit   
                   """)


def Yes_No():
    print("Are you want to continue?")
    print("""
               1.Yes
               2.No          
               """)


import time
print("Welcome to Mobile Banking Management System")
print("Wait few second...........")
time.sleep(1)
password = 1234
pin = int(input("Enter your password :"))
balance = 500
if password==pin :
    run()
    while True :


        try:
            option = int(input("Enter your choice :"))

        except:
            print("Please enter valid option.")
        # For current  balance
        if option == 1:



            print(f"Your current balance is {balance}")
            Yes_No()
            response = int(input("Enter your choice : "))
            if response==1:
                run()

            else:
                break
        # For Cash out
        elif option == 2:
            receiver = int(input("Enter Agent number:"))
            Cash_in = int(input("Enter amount:"))
            if Cash_in< balance:
                print("Wait.................")
                time.sleep(2)
                print(f"Cash out {Cash_in} is succesfull")
                print(f"Your current balance is {balance - Cash_in}")
                balance = balance - Cash_in
                Yes_No()
                response = int(input("Enter your choice : "))
                if response == 1:
                    run()

                else:
                    break
            else:
                print("Transaction is not possible.")
                Yes_No()
                response = int(input("Enter your choice : "))
                if response == 1:
                    run()

                else:
                    break

        # For send money
        elif option == 3:
            number = int(input("Enter receiver number:"))
            send_money= int(input("Enter amount:"))


            if send_money<balance :
                print(f"{send_money}taka in {number} is successful")
                print(f"Your current balance is {balance-send_money} taka")
                balance = balance - send_money
                Yes_No()
                response = int(input("Enter your choice : "))
                if response == 1:
                    run()

                else:
                    break
            else:
                print("Transaction is not possible.")
                Yes_No()
                response = int(input("Enter your choice : "))
                if response == 1:
                    run()

                else:
                    break
        # For Mobile Recharge
        elif option == 4:
            number = int(input("Enter mobile number:"))
            Mobile_recharge = int(input("Enter recharge amount:"))
            if Mobile_recharge <= balance:
                print(f"{Mobile_recharge} taka in 0{number} is successful")
                print(f"Your current balance is {balance - Mobile_recharge} taka")
                balance = balance - Mobile_recharge
                Yes_No()
                response = int(input("Enter your choice : "))
                if response == 1:
                    run()

                else:
                    break
            else:
                print("Mobile Recharge is not possible.")
                Yes_No()
                response = int(input("Enter your choice : "))
                if response == 1:
                    run()

                else:
                    break
        # For pay bill

        # ---------------------------------------------

        elif option == 5:

            #pay_bill(balance)
            c = pay_bill(balance)
            balance=c



        # For end program

        elif option == 6 :

            m_number=input("Enter Marchent account number : ")
            payment = int(input("Enter amount : "))

            if payment <= balance:
                print(f"""
                Payment {payment} is successful.
                Rest of balance is {balance-payment} taka.
                                
                """)
                balance = balance - payment
                Yes_No()
                response = int(input("Enter your choice : "))
                if response == 1:
                    run()

            else :
                print("You have not enough money .")
                print("Payment is not possible.")
                Yes_No()
                response = int(input("Enter your choice : "))
                if response == 1:
                    run()


        elif option==7:
            break

else:
    print("Wrong pin please  try again.")



