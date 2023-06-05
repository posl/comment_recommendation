def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == '0':
            ans += 1
    print(min(ans + K * 2, N - 1))

if __name__ == '__main__':
    main()