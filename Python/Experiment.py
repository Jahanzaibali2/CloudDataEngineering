# print("rana")
# x = 7/3
# y = 7//3
# print(x)
# print(y)

# yearsOfService = int(input("Enter your year's of service: "))
# Salary = int(input("Enter your Salary: "))

# if yearsOfService >= 5:
#     Salary = Salary*0.05
#     print(f"Your recieved a 5% bonus, your salary for this month is {Salary}")

# else:
#     print("You're not eligible")


strInput = input("Enter a string: ")
print("--------")
print("--------")
print("--------")
print("--------")
print("--------")


def Counter(strInput) : 
    countUpper = 0
    countLower = 0
    for i in strInput:
        if (i.islower()):
            countLower += 1
        else : 
            countUpper += 1
    print(f"Number of uppercase letters: {countUpper}")
    print(f"Number of lowercase letters: {countLower}")
    return countUpper,countLower

Counter(strInput)
