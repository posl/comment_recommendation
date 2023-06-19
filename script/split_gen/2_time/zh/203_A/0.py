def get_input():
    while True:
        try:
            a, b, c = input().split()
            a = int(a)
            b = int(b)
            c = int(c)
            if 1 <= a <= 6 and 1 <= b <= 6 and 1 <= c <= 6:
                return a, b, c
            else:
                print("输入错误，请重新输入")
        except:
            print("输入错误，请重新输入")
