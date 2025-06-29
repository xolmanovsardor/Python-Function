def add(a,b):
    result = a + b
    return result
 
def subtract(a,b):
    result = a - b
    return result

def multiply(a,b):
    result = a * b
    return result

def divide(a,b):
    result = a / b
    return result

a = int(input())

b = input("(+,-,*,/)")

c = int(input())

if b == "+":
    print(add(a , c))

elif b == "-":
    print(subtract(a,c))

elif b == "*":
    print(multiply(a,c))

elif b == "/":
    print(divide(a,c))
