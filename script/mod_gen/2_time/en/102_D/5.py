def main():
    N = int(input())
    A = list(map(int,input().split()))
    S = [0]
    for i in range(N):
        S.append(S[i]+A[i])
    ans = 10**18
    for i in range(1,N-1):
        for j in range(i+1,N):
            P = S[i]
            Q = S[j]-S[i]
            R = S[-1]-S[j]
            ans = min(ans,max(P,Q,R)-min(P,Q,R))
    print(ans)

if __name__ == '__main__':
    main()