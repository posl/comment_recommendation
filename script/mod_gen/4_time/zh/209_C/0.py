def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    ans = 1
    for i in range(n):
        ans *= c[i] - i
        ans %= 1000000007
    print(ans)

if __name__ == '__main__':
    main()