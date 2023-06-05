def multi():
    a,b = input().split()
    a = int(a)
    b = int(b)
    if a >= 1 and a <= 100 and b >= 1 and b <= 100:
        print(a*b)
    else:
        print("输入的数值不符合要求")
