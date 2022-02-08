#rollercoaster ride


print("welcome to rollercoaster ride")
height=int(input("enter your height in cm\n"))
age=int(input("enter your age in years\n"))
if(height>=120):
   print("you're allowed for the ride")
   if(age<=12):
       print("Enjoy the ride kiddo pay 5$ price")
       
   if(age<18):
       print("you neeed to pay 7$ only!")
   if(age>=18):
    print("You're an adult pay full price 12$")
   
else:
    print("you aren't allowed for this ride sorry!")
    