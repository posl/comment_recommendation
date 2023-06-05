def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[i] = a[i] - (i + 1)
    b.sort()
    if n % 2 == 1:
        ans = 0
        for i in range(n):
            ans += abs(b[i] - b[n // 2])
        print(ans)
    else:
        ans1 = 0
        for i in range(n):
            ans1 += abs(b[i] - b[n // 2])
        ans2 = 0
        for i in range(n):
            ans2 += abs(b[i] - b[n // 2 - 1])
        print(min(ans1, ans2))

if __name__ == '__main__':
    main()