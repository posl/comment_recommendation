def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == "0":
            j = i
            while j < N and S[j] == "0":
                j += 1
            ans = max(ans, j - i)
    print(min(ans + 2 * K, N))
main()
