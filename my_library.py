def addition(*args):
    result = 0
    for x in args:
        result+=x
    return result

def subtraction(*args):
    result = 0
    for x in args:
        result-=x
    return result

def factorial(n):
    if n == 0:        
        return 1      
    else:      
        return n * factorial(n-1)
