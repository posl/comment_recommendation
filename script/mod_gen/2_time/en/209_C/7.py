def main():
    N = int(input())
    C = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    ans = 1
    prev = 0
    for i in range(N):
        if prev == C[i]:
            ans = ans * (C[i] - 1) % mod
        elif prev + 1 == C[i]:
            ans = ans * C[i] % mod
        elif prev < C[i]:
            ans = ans * C[i] * (C[i] - 1) // 2 % mod
        else:
            ans = 0
        prev = C[i]
    print(ans)

if __name__ == '__main__':
    main()