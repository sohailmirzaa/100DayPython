#this is an adventure game made with python 
# import pyfiglet module
import pyfiglet

result = pyfiglet.figlet_format("Adventure Game")
print(result)


print("Adventure game")
print("Instructions")
print("1.You have two choices to slect from if you slect good choices you will end up winning the game \n")
choice=input("Enter the number of your choice \n")
if(choice=="1"):
    print("want to go to island or quit the game?")
    x=input("yes=1 no=0 \n")
    if(x=="1"):
        print("You're going to the island alone")
        y=input(" enter you choice\n")
        if(y=="1"):
             print("you have reached the island successfully")
             print("choose from option 1 and 2")
             print("1.Go for adventure")
             print("2.go for sun bathing")
             x=input("Enter you choice\n")
             if(x=="1"):
                 print("your're going for adventure and you found a map")
                 print("1.open the map")
                 print("2.throw the map")
                 x=input("Enter choices\n")
                 if(x=="1"):
                     print(" you find the location of the treasure")
                     print("1.Take the boat 100$")
                     print("2.go swiming")
                     x=input("Enter you choices\n")
                     print(" you find the location of the treasure")
                     if(x=="1"):
                           print("You successfull foun the trease no you're millionaire")
                     else:
                          print("you have been killed by the aligators")

             else:
                     print("you have been killed by pirates")
                
                

        
                
    else:
        print("exiting to main menu")          




