def main():
    #读取输入
    n,p,q,r,s = map(int,input().split())
    a = list(map(int,input().split()))
    #解决问题
    b = a.copy()
    for i in range(p-1,q):
        b[i] = a[r-1+i-q]
    for i in range(r-1,s):
        b[i] = a[p-1+i-r]
    #输出结果
    print(*b)

if __name__ == '__main__':
    main()