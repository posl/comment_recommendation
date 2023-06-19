def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [a[i] - i - 1 for i in range(n)]
    b.sort()
    if n % 2 == 1:
        ans = sum([abs(b[n // 2] - b[i]) for i in range(n)])
    else:
        ans = min(sum([abs(b[n // 2] - b[i]) for i in range(n)]), sum([abs(b[n // 2 - 1] - b[i]) for i in range(n)]))
    print(ans)

if __name__ == '__main__':
    main()