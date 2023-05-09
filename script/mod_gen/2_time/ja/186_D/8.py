def main():
    n = int(input())
    a = list(map(int,input().split()))
    if n == 2:
        print(abs(a[0]-a[1]))
        return
    a.sort()
    ans = 0
    for i in range(n):
        ans += (n-i-1)*a[i] - i*a[i]
    print(ans)

if __name__ == '__main__':
    main()