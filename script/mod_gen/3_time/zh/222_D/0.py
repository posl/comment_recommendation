def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 1
    for i in range(n):
        ans *= max(0, b[i] - a[i] + 1)
        ans %= 998244353
    print(ans)

if __name__ == '__main__':
    main()