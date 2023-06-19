def problem229_b():
    a,b = input().split()
    a = int(a)
    b = int(b)
    if a+b >= 10**10:
        print("Hard")
    else:
        print("Easy")

if __name__ == '__main__':
    problem229_b()