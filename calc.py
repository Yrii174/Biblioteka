#
def calculate(a, b, op='+'):
    print("Welcome to the Python Calculator")
    
    return op1(a, b, op) 

# def op(a, b, op):
#     if op=='+' or op=='sum':
#         return opSum(a, b)
#     #return op(a, b)
    
def op1(a, b, op):
    a=complex(a)
    b=complex(b)
    if op=='+' or op=='sum':
        return opSum(a, b)
    if op=='-' or op=='sub':
        return opSub(a, b)
    if op=='*' or op=='mul':
        return opMul(a, b)
    if op=='/' or op=='div':
        return opDiv(a, b)
    if op=='%' or op=='div5':
        return opDiv5(a, b)
    if op=='**' or op=='pow':
        return opPow(a, b)
    if op=='//' or op=='div7':
        return opDiv7(a, b)
    if op=='==' or op=='eq':
        return opEq(a, b)
    if op=='sqrt' or op=='sqr':
        return opSqrt(a)

def opSum(a, b):
    return a + b
def opMul(a, b):
    return a * b
def opSub(a, b):
    return a - b
def opDiv(a, b):
    return a / b
def opDiv5(a, b):
    return a % b
def opPow(a, b):
    return a ** b
def opDiv7(a, b):
    return a // b
def opEq(a, b):
    return a == b
def opSqrt(a):
    return (a**0.5)
#def op10(a, b):
