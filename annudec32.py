'''
author name:annu james
date:3/12/24
'''
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
factorial(5)
print(factorial(5))