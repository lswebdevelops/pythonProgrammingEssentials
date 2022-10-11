"""
calculates the  Collatz conjecture using python
"""


# def f(n):
#     return n // 2 if n % 2 == 0 else 3*n + 1
#or
def f(n):
# f(n)
# if n even divide it by 2
# if n odd > multiply n by 3 and adds one to the result.

    if n % 2 == 0:
        return n // 2 
    else:
        return 3 * n + 1

print(f(f(f(f(f(f(f(674))))))))



print(f(f(f(f(f(f(f(f(f(f(f(f(f(f(1071)))))))))))))))