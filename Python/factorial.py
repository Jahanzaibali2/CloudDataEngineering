num = int(input("enter the number you want thr factorial of : "))

def factorial(num):
    if num == 1:
        return num
    else:
        return num*factorial(num - 1)




print(factorial(num))