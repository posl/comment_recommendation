def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    cnt = 1
    for i in range(1,n):
        if a[i] == a[i-1]:
            cnt += 1
        else:
            ans += cnt * (n-i)
            cnt = 1
    print(ans)

if __name__ == '__main__':
    main()