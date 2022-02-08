#tip calculator

billAmount=input("Enter the bill amount\n")
Tip=input("Enter the amount of tip to be paid in 12% 15% 18%\n")
Tip= float(Tip)/100
# print(Tip)
TipPercent= float(billAmount)*(Tip)
currentBill= float(billAmount)+float(TipPercent)
NoOfPerson=input("number of person to split with\n")
currentBill=currentBill/ float(NoOfPerson)
print(f"The total bill amount per head is {currentBill}")
