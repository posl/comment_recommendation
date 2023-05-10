def main():
    n = int(input())
    a = tuple(map(int, input().split()))
    b = tuple(map(int, input().split()))
    ans = 1
    for i in range(n):
        ans *= max(0, b[i] + 1 - a[i])
        ans %= 998244353
    print(ans)

if __name__ == '__main__':
    main()