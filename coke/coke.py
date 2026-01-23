due=50
while due > 0:
    print(f"Amount Due: {due}")
    coin=int(input("Insert Coin:"))
    if coin in [25,10,5]:
        due-=coin
change=abs(due)
print(f"Change Owed: {change}")

