print("rana")
x = 7/3
y = 7//3
print(x)
print(y)
yearsOfService = int(input("Enter your year's of service: "))
Salary = int(input("Enter your Salary: "))

if yearsOfService >= 5:
    Salary = Salary*0.05
    print(f"Your recieved a 5% bonus, your salary for this month is {Salary}")

else:
    print("You're not eligible")
