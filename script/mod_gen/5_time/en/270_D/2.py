def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * (n+1)
    for i in a:
        b[i] = 1
    for i in range(n):
        b[i+1] += b[i]
    ans = 0
    for i in range(k):
        ans += b[n] - b[a[i]]
        n -= a[i]
    print(ans)
    return

if __name__ == '__main__':
    main()