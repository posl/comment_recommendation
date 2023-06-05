def solve():
    #读取输入
    a1,a2,a3,a4 = map(int,input().split())
    #处理
    if a1+a2+a3+a4 <= 100:
        print(4)
    elif a1+a2+a3 <= 100:
        print(3)
    elif a1+a2 <= 100:
        print(2)
    elif a1 <= 100:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    solve()