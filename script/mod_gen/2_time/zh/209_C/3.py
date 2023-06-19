def main():
    n = int(input())
    c = list(map(int, input().split()))
    ans = 1
    c.sort()
    for i in range(n):
        ans *= max(c[i] - i, 0)
        ans %= 1000000007
    print(ans)

if __name__ == '__main__':
    main()