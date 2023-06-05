def main():
    N,K = map(int,input().split())
    s = input()
    #print(N,K,s)
    s = list(s)
    #print(s)
    ans = 0
    for i in range(N-1):
        if s[i] == s[i+1]:
            ans += 1
    ans = min(ans+2*K,N-1)
    print(ans)

if __name__ == '__main__':
    main()