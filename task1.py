# budget task

item1 = int(input("enter first item price: "))
item2 = int(input("enter second item price: "))
item3 = int(input("enter third item price: "))

budget = int(input("enter your budget: "))

total = item1 + item2 + item3

print("total =", total)

if total > budget:
    print("you exceeded your budget by", total - budget)
elif total < budget:
    print("you have", budget - total, "left")
else:
    print("you spent exactly your budget")

input("press enter to exit")