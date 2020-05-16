print("Welcome")


Initial_Blanace=1000
Balance = Initial_Blanace
chances=2;
ATM = True
while chances>0:
    ATM = True
    pin = int(input("Enter the Pin"))
    restart = 'y'
    flag = False
    flag1= False
    if pin == 1234:
        print("Please press 1 to check Balance")
        print("Please press 2 to Withdraw")
        print("Please press 3 to put Amount")
        print("please press 4 to Exit")

        while restart not in ['no','NO','N','n']:
            choice = int(input("Enter Your choice "))
            if choice == 1:
                
                print("Your Balance",Balance)
                
                value=input("Would you lke to restart ")
                restart = value
                if restart not in ['no','NO','N','n']:
                    chances = chances-1
                    break
                else:
                    flag = True
                    break

            elif choice == 2:
                Withdraw = int(input("Enter the Amount to withdraw "))
                if Withdraw < Balance:
                    print("Amount ",Withdraw," is withdrwan")
                    Balance = Balance-Withdraw
                    print("Balance ->",Balance)
                else:
                    print("Your Amount Less")

                
                value=input("Would you lke to restart ")
                restart = value
                if restart not in ['no','NO','N','n']:
                    chances = chances-1
                    break
                else:
                    flag = True
                    break
            
            elif choice == 3:
                credit = int(input("Enter the Amount you like to put "))
                print("Amount ",credit,"credited")
                Balance = Balance+credit
                print("Balance ->",Balance)

                value=input("Would you lke to restart ")
                restart = value
                if restart not in ['no','NO','N','n']:
                    chances = chances-1
                    break
                else:
                    flag = True
                    break
                
            elif choice == 4:
                flag = True
                break

    else:
        print("Invalid Pin")


    if flag == True:
        print("Thank You")
        break
    else:
        continue          

if chances == 0:
    print("Your Chances is Over")






