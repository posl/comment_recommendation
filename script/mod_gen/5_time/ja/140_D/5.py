def main():
    N, K = map(int, input().split())
    S = input()
    cnt = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            cnt += 1
    ans = min(cnt + 2*K, N-1)
    print(ans)

if __name__ == '__main__':
    main()