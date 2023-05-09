def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == 'L':
            ans += 1
            if i+1 < N and S[i+1] == 'R':
                ans += 1
        else:
            if i+1 < N and S[i+1] == 'L':
                ans += 1
    print(min(2*N-1, ans+2*K))

if __name__ == '__main__':
    main()