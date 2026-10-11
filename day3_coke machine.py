due=50
while due>0:
    print("Amount due:",due)
    coin=int(input("enter the coin:"))
    if coin==25 or coin==10 or coin==5:
        due=due-coin
print("change owed:",-due)
