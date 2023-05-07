def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == '0':
            ans += 1
            if i + 1 < N and S[i + 1] == '1':
                ans += 1
    if ans == 0:
        print(N - 1)
    else:
        print(min(ans + 2 * K, N))

if __name__ == '__main__':
    main()