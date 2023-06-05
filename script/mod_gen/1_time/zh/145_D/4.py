def main():
    #输入
    x,y = map(int,input().split())
    #求解
    ans = 0
    if (x+y)%3 == 0:
        if x<=y*2 and y<=x*2:
            ans = 1
            for i in range(1,x):
                ans = ans*(x+y-i)%1000000007
                ans = ans*pow(i,1000000005,1000000007)%1000000007
    #输出
    print(ans)

if __name__ == '__main__':
    main()