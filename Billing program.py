# Shop Bill
items = [100, 50, 200] # 3 items
total = 0

for price in items:
    total = total + price

print("Total =", total) # 350

# Discount using bitwise trick
# 10% discount = total - total//10
discount = total // 10
final_bill = total - discount

print("Discount =", discount)
print("Final Bill =", final_bill)

# Check bill even/odd
if (final_bill & 1) == 0:
    print("Bill is EVEN - give toffee")
else:
   # OUTPUT:
# Total = 350
# Discount = 35
# Final Bill = 315
# Bill is ODD print("Bill is ODD")
