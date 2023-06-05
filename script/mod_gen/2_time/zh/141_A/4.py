def main():
    N, K = map(int, input().split())
    S = input()
    #print(N, K, S)
    ans = 0
    for i in range(1, N):
        if S[i - 1] == S[i]:
            ans += 1
    ans += 2 * K
    print(min(ans, N - 1))

if __name__ == '__main__':
    main()