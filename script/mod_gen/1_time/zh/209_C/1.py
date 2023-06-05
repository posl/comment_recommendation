def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    m = 10**9 + 7
    ans = 1
    for i in range(n):
        ans *= max(0, c[i] - i)
        ans %= m
    print(ans)

if __name__ == '__main__':
    main()