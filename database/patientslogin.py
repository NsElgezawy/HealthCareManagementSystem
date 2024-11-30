#Ashraf-check if Name is valid in table database
def checkname(name):
    for i in name: 
        if not (i.isalpha() or i.isspace()):
            return False
    return True 
# Anas Mohamed - check if the age is valid integer not a string 
## first way ##
# def input_age(age):
#     if not age.isdigit():  
#         print("Invalid input")  
#         return None  
#     else:
#         return int(age)  
## second way ##
def input_age(age):
    try:
        return int(age)  
    except ValueError:
        print("Invalid input")
        return None

