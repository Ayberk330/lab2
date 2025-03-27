import math


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n = int(input("enter n"))
print(factorial(n))

def lambdafunction(x,n):
    x1=(-1)** n
    x2=(x)**((2*n)+1)
    x3=factorial((2*n)+1)
    result =x1*x2/x3
    return result

def  sine_x(x,n):
    radians=x * math.pi / 180.0
    res =0
    for i in range(n):
        res += lambdafunction(radians,i)

    return res
x=int(input("enter x"))
n=int(input("enter n"))
print(sine_x(x,n))

result = 0.0

result = 0.0

def recfunc(n):
    """
    Your function should take “n” as a parameter
    """
    global result
    if n == 0:
        print("The harmonic sum is:", result)
        return
    result += 1 / n
    recfunc(n - 1)

n = int(input("Enter n: "))
recfunc(n)

print(recfunc.__doc__)



