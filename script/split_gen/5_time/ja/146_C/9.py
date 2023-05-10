def main():
    a,b,x = map(int,input().split())
    if a * 10 + b * 1 > x:
        print(0)
        exit()
    elif a * 10 ** 9 + b * 10 > x:
        print(10 ** 9)
        exit()
    else:
        for i in range(10,0,-1):
            if a * i * 10 ** (i - 1) + b * i <= x:
                print(i * 10 ** (i - 1))
                exit()
