# Electricity Bill Calculator
RATE = 12.90
name = input("Enter customer name: ")

if name.strip() == "":
 print("invalid name")
 name = input("enter student name: ")
 
 
previous = input("Enter previous meter reading: ")
  
if not previous.isdigit() or not (0 <= int(previous) <= 1000):
    print("invalid integer")
    previous = input("Enter previous meter reading: ")
    
    
current = input("Enter current meter reading: ")

if not current.isdigit() or not (0 <= int(current) <= 1000):
    print("invalid integer")
    current = input("Enter previous meter reading: ")

current1 = int(current)
previous1 = int(previous)
consumption = current1 - previous1
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))

# Validation rules
# 1. Customer name -- Must not be empty
# 2. Previous reading -- Number at least 0
# 3. Current reading -- Number at least the previous reading
