def main():
    N = int(input())
    W = list(map(int, input().split()))
    S1 = 0
    S2 = sum(W)
    ans = S2
    for i in range(N-1):
        S1 += W[i]
        S2 -= W[i]
        ans = min(ans, abs(S1-S2))
    print(ans)

if __name__ == '__main__':
    main()