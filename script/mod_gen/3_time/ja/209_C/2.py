def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    ans = 1
    for i in range(n):
        ans *= max(c[i] - i, 0)
        ans %= 10**9 + 7
    print(ans)

if __name__ == '__main__':
    main()