#Day In life calculator

currentAge=input("Enter you current age\n")
yearsleft=(90- int (currentAge))
oneYearInDays= int (365)*yearsleft
MonthsInYear= int (12)*yearsleft
weekInYear= int (52)*yearsleft

print(f"you have {yearsleft} years, {oneYearInDays} Days, {MonthsInYear} Months, {weekInYear} Weeks")