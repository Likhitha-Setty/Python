def factorial(a):
    if a==0 or a==1:
        return 1
    else:
        return a*factorial(a-1)
a=int(input("Enter a number: "))
print("Factorial of {} is: {}".format(a,factorial(a)))
