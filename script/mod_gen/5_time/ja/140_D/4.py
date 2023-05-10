def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N-1):
        if S[i] != S[i+1]:
            ans += 1
    ans = min(N-1, ans+2*K)
    print(ans)
main()

if __name__ == '__main__':
    main()