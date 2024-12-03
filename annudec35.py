'''
author name:annu james
date:3/12/24
'''
def gcd_numbers(n1,n2):
    if n1%n2==0:
        return n2
    else:
        return gcd_numbers(n2,n1%n2)
print(gcd_numbers(1220,516))