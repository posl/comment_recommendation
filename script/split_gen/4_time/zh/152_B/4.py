def problem152_b():
    a,b = input().split()
    a = int(a)
    b = int(b)
    if a == b:
        print(str(a)*a)
    elif a > b:
        print(str(b)*a)
    else:
        print(str(a)*b)
problem152_b()
