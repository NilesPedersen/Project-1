'''
all these functions serve as mathmatical functions that recieve the number of said items and they all return their total as a string
'''
def cookie_function(num):
    total = f'{num * 1.50:.2f}'
    return total

def sandwich_function(num):
    total = f'{num * 4.00:.2f}'
    return total

def water_function(num):
    total = f'{num * 1.00:.2f}'
    return total

def soda_function(num):
    total = f'{num * 1.75:.2f}'
    return total

def cart_total(num1, num2, num3, num4):
    num1 = num1 * 1.50
    num2 = num2 * 4.00
    num3 = num3 * 1.00
    num4 = num4 * 1.75
    total = f'{num1 + num2 + num3 + num4:.2f}'
    return total


