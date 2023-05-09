def main():
    N = int(input())
    C = list(map(int, input().split()))
    mod = 10**9 + 7
    ans = 1
    for i in range(N):
        if i == 0:
            ans *= C[i]
        else:
            ans *= max(0, C[i] - C[i - 1] + 1)
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()