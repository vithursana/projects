#TASK 1
# write a balance input with money in account
# create a varaible with a pin
# promot the user to enter pin
# if pin is correct then display balance
# if pin is wrong then notify user

#Extensions
# if pin matches give user a prompt to withdraw money/ deposit
# ask for input money
# subtract or add money to balance 
# display new balance
# end code

balance = 20229

print("What is your pin?")
#print("What is your favourite animal?")
input_animal= input()

# if pin is correct displays balance and asks to withdra/deposit money
# asks for user input
if input_animal == "1234":
    print("Your balance is", balance, "have a good day!")
    print("Would you like to deposit or withdraw money?")
    input_withdraw=input()

# to withdraw subtracts user input to balance and displays new balance
    if input_withdraw == "withdraw":
        print ("How much?")
        money_w = int(input())
        new_balancee = (balance - money_w)
        print("Your balance is", new_balancee, "have a good day!")

# to deposit adds user input to balanc eand displays new balance
    elif input_withdraw == "deposit":
        print("How much?")
        money_add= int(input())
        new_balance = int(balance) + int(money_add)
        print("Your new balance is", new_balance, "Enjoy your day!")

    
else:
        print ("Wrong try again")