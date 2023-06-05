def main():
    #读入数据
    a,b,c,d=map(int,input().split())
    #判断是否有解
    if b>=a:
        print(-1)
        return
    #二分查找
    left=0
    right=10**18
    while right-left>1:
        mid=(left+right)//2
        if mid*d>=a:
            right=mid
        else:
            left=mid
    print(b*(right-1)+c*(right-1))

if __name__ == '__main__':
    main()