def calcurate(price, tax=0.1):
    tax = price*tax
    total = price + tax
    print(f"{total}円")

price = int(input("price: "))
calcurate(price)
