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

def recfunc(n):
    """Your function should take “n” as a parameter but returns nothing."""
    reslt=0

    for i in range(n):
        reslt +=1/n
        n-=1
    print(reslt)


n=int(input("enter n"))
print(recfunc(n))

print(recfunc.__doc__)

