# *args returns  a tupple
def addition(*args):
    result = 0
    for x in args:
        result+=x
    return result

# enumerate() adds a counter to an iterable and returns it in a form of enumerate object.
#This enumerate object can then be used directly in for loops or 
#be converted into a list of tuples using list() method.
def subtraction(*args):
    result = list(args)
    res = result[0]
    for x, y in enumerate(result):
        print(x,y)
        try:
            res = res - result[x+1]
        except IndexError:
            pass
    return res

def factorial(n):
    if n == 0:        
        return 1      
    else:      
        return n * factorial(n-1)
