expenses = [10.50, 8, 5, 15, 20, 5, 3]
# sum = 0

# for x in expenses: 
#     sum = sum + x


# print("you spent $", sum, " on lunch this week.", sep='')

# total = sum(expenses)

total = 0
expenses = []
# for i in range(7):
#     expenses.append(float(input("enter an expense:")))

# total = sum(expenses)
# print("you spent $", total, sep='')

num_expenses = int(input("enter # of expenses:"))
for i in range(num_expenses):
    expenses.append(float(input("enter an expense:")))

total = sum(expenses)
print("you spent $", total, sep=" ")