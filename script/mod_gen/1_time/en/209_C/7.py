def main():
    N = int(input())
    C = list(map(int, input().split()))
    if N == 1:
        print(1)
        return
    MOD = 10**9 + 7
    C.sort()
    if C[0] == 1:
        print(0)
        return
    ans = 1
    for i in range(N):
        ans *= (C[i] - i)
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()