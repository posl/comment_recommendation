def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == 'L':
            ans += 1
        else:
            break
    for i in range(N-1, -1, -1):
        if S[i] == 'R':
            ans += 1
        else:
            break
    ans = min(ans + 2*K, N)
    print(ans)

if __name__ == '__main__':
    main()