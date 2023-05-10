def main():
    x,y,n = map(int,input().split())
    ans = 10000000000000
    for i in range(0,n+1):
        ans = min(ans,((n-i)*x)+(i*3*y))
    print(ans)

if __name__ == '__main__':
    main()