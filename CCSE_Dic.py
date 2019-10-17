import json

courses=json.load(open("CCSE_Courses.json"))
x="y"
while(x=="y"):
    user_input=input("Enter The course code and number:").replace(" ","").strip().lower()
    if user_input in courses.keys():
        print(courses[user_input])
    else:
        print("No Course Found, check the code & the number")
    x=input("Search Another Course?(y/n)")
