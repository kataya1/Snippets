def add(*args):
    return sum(args)

def div(a,b):
    if(b==0): raise ZeroDivisionError 
    return a/b