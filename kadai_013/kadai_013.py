def calculate(price, tax=0.1):
    total_price = price + (price * tax)
    return total_price
    
calculate(1000, 0.1)
