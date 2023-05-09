def solve():
    N = int(input())
    X = [0]*N
    Y = [0]*N
    for i in range(N):
        X[i],Y[i] = map(int,input().split())
    #print(X)
    #print(Y)
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if X[i]*(Y[j]-Y[k])+X[j]*(Y[k]-Y[i])+X[k]*(Y[i]-Y[j]) != 0:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    solve()