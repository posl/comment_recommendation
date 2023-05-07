def main():
    N, K = map(int, input().split())
    S = input()
    S = S + S
    ans = 0
    for i in range(N):
        if S[i] == "R":
            ans += 1
            if S[i+1] == "L":
                ans += 1
    if ans == N:
        ans = N - 1
    ans = min(ans + 2 * K, N)
    print(ans)

if __name__ == '__main__':
    main()