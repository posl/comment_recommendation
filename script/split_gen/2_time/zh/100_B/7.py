def main():
    #读取输入
    d,n = map(int, input().split())
    #计算
    if d == 0:
        if n == 100:
            print(101)
        else:
            print(n)
    elif d == 1:
        if n == 100:
            print(10100)
        else:
            print(n*100)
    else:
        if n == 100:
            print(1010000)
        else:
            print(n*10000)
