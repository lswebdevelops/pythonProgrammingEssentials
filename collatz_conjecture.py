"""
calculates the  Collatz conjecture using python
"""

# f(n)
# if n even divide it by 2
# if n odd > multiply n by 3 and adds one to the result.
# 
# 
# def f(n):
   
#     while n != 1:
#         if n % 2 == 0:
#             n = n // 2
#         elif (n % 2 == 1):
#             n = (n * 3 )+ 1
#         else:
#             print("something went very wrong!")
#             return None
#     return n



# def f(n):
#     return n // 2 if n % 2 == 0 else 3*n + 1
#or
def f(n):
  
    if n % 2 == 0:
        return n // 2 
    else:
        return 3 * n + 1

print(f(f(f(f(f(f(f(674))))))))



print(f(f(f(f(f(f(f(f(f(f(f(f(f(f(1071)))))))))))))))