def lcd(a,b):
    a, b = (a, b) if a > b else (b, a)
    while b > 0:
        a, b = b, a % b
    return a
a,b=map(int,input().split(" "))
print(a*b//lcd(a,b))
