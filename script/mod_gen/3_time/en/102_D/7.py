def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += a[i]
    ans = 10**10
    p = 0
    for i in range(n-1):
        p += a[i]
        ans = min(ans, abs(sum - p - p))
    print(ans)

if __name__ == '__main__':
    main()