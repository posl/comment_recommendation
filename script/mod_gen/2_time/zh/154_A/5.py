def main():
    #输入
    s,t = input().split()
    a,b = map(int,input().split())
    u = input()
    #处理
    if s == u:
        a -= 1
    elif t == u:
        b -= 1
    #输出
    print(a,b)

if __name__ == '__main__':
    main()