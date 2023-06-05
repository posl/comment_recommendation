def problem127_a():
    a,b = map(int,input().split())
    if a >= 13:
        print(b)
    elif 6 <= a <= 12:
        print(int(b/2))
    elif a <= 5:
        print(0)
    else:
        print("error")
