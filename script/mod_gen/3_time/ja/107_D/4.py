def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        b.append(a[i] - i - 1)
    b.sort()
    m = b[n//2]
    ans = 0
    for i in range(n):
        ans += abs(a[i] - (m + i + 1))
    print(ans)

if __name__ == '__main__':
    main()