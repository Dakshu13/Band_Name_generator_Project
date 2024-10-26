# PROJECT - BAND NAME GENERATOR PROJECT
print("Welcome to band generator simple application!")
# print a statement to welcome your viewers into your application
#Now, ask the user to enter the name of the city, they grew up and store it as a variable
city = input("Enter the name of the city, they grew up?\n")
#Now, ask the user to enter stylist name to suit the city? For instance, use like sunrisers, eagles, knights etc.
style = input("Enter the name which suits the city?\n")
#concate both the results of the variable and store it a new variable
generator_name = city + " " + style
#Now, print the generated name
print("The generated name is:"+ generator_name)