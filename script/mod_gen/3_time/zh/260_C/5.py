def main():
    n,x,y = map(int,input().split())
    ans = 0
    for i in range(1,n):
        if i <= y:
            ans += (n-i)*x
        else:
            ans += (n-i)*y
    print(ans)

if __name__ == '__main__':
    main()