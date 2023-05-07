def main():
    N = int(input())
    S = input()
    W = list(map(int,input().split()))
    #print(N,S,W)
    #print(S[0])
    #print(W[0])
    #print(W)
    #print(W[0:3])
    #print(W[3:5])
    ans = 0
    for X in range(1,10**9+1):
        #print(X)
        #print(W[0:X])
        #print(W[X:N])
        #print(S[0:X])
        #print(S[X:N])
        #print(W[0:X])
        #print(W[X:N])
        #print(S[0:X])
        #print(S[X:N])
        #print(sum(W[0:X]))
        #print(sum(W[X:N]))
        #print(sum(S[0:X]))
        #print(sum(S[X:N]))
        if sum(W[0:X]) < X*sum(S[0:X]):
            #print("a")
            continue
        if sum(W[X:N]) >= X*sum(S[X:N]):
            #print("b")
            continue
        ans = max(ans,sum(S[0:X])+sum(S[X:N]))
        #print(ans)
    print(ans)

if __name__ == '__main__':
    main()