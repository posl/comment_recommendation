def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == "R":
            if i == 0:
                ans += 1
            else:
                if S[i - 1] == "L":
                    ans += 1
    for i in range(N - 1, -1, -1):
        if S[i] == "L":
            if i == N - 1:
                ans += 1
            else:
                if S[i + 1] == "R":
                    ans += 1
    ans = min(ans + 2 * K, N)
    print(ans)

if __name__ == '__main__':
    main()