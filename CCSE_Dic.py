#import json library
import json

#load dictionary from json file
courses=json.load(open("CCSE_Courses.json"))

#check if the user want to repeat the search
repeat="y"

#if yes
while(repeat=="y"):
    #get the code and the number of the course, remove spaces from left,right and in the middle
    #make all the input in lower case
    user_input=input("Enter The course code and number:").replace(" ","").strip().lower()
    
    #if user enters an existed course
    if user_input in courses.keys():
        #Course name and department is printed here
        print(courses[user_input])
    #if user enters a wrong course name
    else:
        print("No Course Found, check the code & the number")
   
    #Ask user if he wants to re-enter another course name   
    repeat=input("Search Another Course? Press y for yes or n for no)")
    if repeat != "n" and repeat !="y":
        repeat=input("PLEASE. Press y for yes or n for no)")
