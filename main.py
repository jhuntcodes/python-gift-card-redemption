# stores balance
balance = 100
# asks and stores users purchase amount 
answer = int(input("Enter Purchase Amount: "))
# program checking user has balance to pay
if answer > balance:
    print("Purchase Denied :(")
else:
    new_balance = balance - answer
    print(f"Purchase Successful! Your new balance is: {new_balance}")