def main():
    n = int(input())
    a = [list(map(int,input().split())) for i in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if -1 <= (a[i][1]-a[j][1])/(a[i][0]-a[j][0]) <= 1:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()