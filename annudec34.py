'''
author name:annu james
date:3/12/24
'''
def product_numbers(n1,n2):
    if n2==1:
        return n1
    else:
        return n1+product_numbers(n1,n2-1)
print(product_numbers(5,4))