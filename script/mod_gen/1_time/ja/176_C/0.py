def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    b[0] = a[0]
    for i in range(1, n):
        b[i] = max(a[i], b[i - 1])
    ans = 0
    for i in range(n):
        ans += b[i] - a[i]
    print(ans)

if __name__ == '__main__':
    main()