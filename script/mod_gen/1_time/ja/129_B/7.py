def main():
    N = int(input())
    W = list(map(int, input().split()))
    W = [0] + W
    S = sum(W)
    S1 = 0
    S2 = S
    ans = 10**10
    for i in range(1, N+1):
        S1 += W[i]
        S2 -= W[i]
        ans = min(ans, abs(S1-S2))
    print(ans)

if __name__ == '__main__':
    main()