def main():
    x,y,n = map(int,input().split())
    ans = 1000
    for i in range(n+1):
        for j in range(n+1):
            if i + j == n:
                ans = min(ans,(x*i)+(y*j))
    print(ans)

if __name__ == '__main__':
    main()