def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        b.append(a[i] - i - 1)
    b.sort()
    if n % 2 == 1:
        k = b[n // 2]
    else:
        k = (b[n // 2] + b[n // 2 - 1]) // 2
    ans = 0
    for i in range(n):
        ans += abs(b[i] - k)
    print(ans)

if __name__ == '__main__':
    main()