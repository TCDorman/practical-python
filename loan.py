
# Get the loan details
money_owed = float(input("How much money do you owe, in dollars?\n")) #50,000
apr = float(input("What is the annual percentage rate? \n")) #3%
payment = float(input("What will your monthly payment be, in dollars? \n"))
months = int(input("how many months do you want to see results for?\n"))

# divide apr by 100 to make it a percent, then divide by 12 to make monthly
monthly_rate = apr/100/12

for i in range(months):
    # add in interest
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    if(money_owed - payment < 0):
        print("The last payment is", money_owed)
        print("You paid off the loan in", i+1, "months" )
        break

    # make payment
    money_owed = money_owed - payment

    # Print the results after this month
    print("paid", payment, "of which", interest_paid, "was interest", end=" ")
    print("Now I owe", money_owed)