def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    ans = 10**9
    for i in range(x[0], x[-1]+1):
        total = 0
        for j in range(n):
            total += (x[j] - i) ** 2
        ans = min(ans, total)
    print(ans)

if __name__ == '__main__':
    main()