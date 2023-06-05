def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 1
    for i in range(n):
        ans *= a[i] - i
        ans %= 1000000007
    print(ans)

if __name__ == '__main__':
    main()