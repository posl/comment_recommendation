def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1, 0, -1):
        if a[i-1] > a[i]:
            ans += a[i-1] - a[i]
            a[i-1] = a[i]
    print(ans)

if __name__ == '__main__':
    main()