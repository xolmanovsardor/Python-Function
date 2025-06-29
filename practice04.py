def get_grade(score):
    result = score
    return result

result = int(input())
if 30 <= result <= 40:
    print("A")
elif 20 <= result <= 29:
    print("B")
elif 10 <= result <= 19:
    print("C")
elif 0 <= result <= 9:
    print("F")
 