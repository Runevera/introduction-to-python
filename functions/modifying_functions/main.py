def apply_discount(price,discount=0.05):
    totaldiscount = price - (price * discount)
    return totaldiscount
def apply_tax(price, tax=0.07):
    totaltax = price + (price * tax)
    return totaltax
def calculate_total(price, discount=0.05, tax=0.07):
    discountedprice = apply_discount(price, discount) 
    totalprice = apply_tax(discountedprice, tax)
    return totalprice


print(f"Total cost with default discount and tax: ${calculate_total(120)}")
print(f"Total cost with custom discount and tax: ${calculate_total(100,discount=0.10,tax=0.08)}")