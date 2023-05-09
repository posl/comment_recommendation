def main():
    MOD = 10**9 + 7
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    ans = 1
    for i in range(n):
        if c[i] < i + 1:
            print(0)
            return
        ans = ans * (c[i] - i) % MOD
    print(ans)

if __name__ == '__main__':
    main()