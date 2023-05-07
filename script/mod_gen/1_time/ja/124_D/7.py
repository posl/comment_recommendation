def main():
    N,K = map(int,input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == "1":
            ans += 1
    ans = min(ans+2*K,N)
    print(ans)

if __name__ == '__main__':
    main()