
# print
print("welcome to the tip calculator....")
total_bill=float(input("What was the total bill? $"))
tip_percent=int(input("How much tip would you like to give? "))
split_bill=int(input("How much people to split the bill? "))

m_bill = (total_bill*(tip_percent/100))+total_bill
pay=round(m_bill/split_bill,2)

print(f"Each person should pay: ${pay}")