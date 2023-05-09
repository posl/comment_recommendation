def main():
    # Input
    N, K = map(int, input().split())
    S = input()
    # Solve
    ans = 0
    for i in range(N):
        if i == 0:
            if S[i] == S[i+1]:
                ans += 1
            else:
                ans += 2
        elif i == N-1:
            if S[i] == S[i-1]:
                ans += 1
            else:
                ans += 2
        else:
            if S[i] == S[i-1] and S[i] == S[i+1]:
                ans += 1
            elif S[i] == S[i-1] or S[i] == S[i+1]:
                ans += 2
            else:
                ans += 3
    ans = min(ans, 2*N-1)
    ans -= 2*K
    ans = max(0, ans)
    # Output
    print(ans)

if __name__ == '__main__':
    main()