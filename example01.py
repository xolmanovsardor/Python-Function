def add_numbers(son1, son2):
    s = son1 + son2
    return s

def sub_numbers(son1, son2):
    s = son1 - son2
    return s

def mul_numbers(son1, son2):
    s = son1 * son2
    return s

def div_numbers(son1, son2):
    s = son1 / son2
    return s

def calculator():
    a = float(input("a = "))
    op = input("operator (+, -, *, /): ")
    b = float(input("b = "))

    if op == '+':
        natija = add_numbers(a, b)
        print(natija)
    elif op == '-':
        natija = sub_numbers(a, b)
        print(natija)
    elif op == '*':
        natija = mul_numbers(a, b)
        print(natija)
    elif op == '/':
        natija = div_numbers(a, b)
        print(natija)
    else:
        print("error op")

calculator()
