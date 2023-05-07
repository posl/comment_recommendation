def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    for i in range(n-1):
        a[i+1] += a[i]
    for i in range(q):
        ans = 0
        for j in range(n):
            ans += abs(a[j] - x[i])
        print(ans)

if __name__ == '__main__':
    main()