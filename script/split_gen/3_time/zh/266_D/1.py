def main():
    #input
    N = int(input())
    T = []
    X = []
    A = []
    for i in range(N):
        t, x, a = map(int, input().split())
        T.append(t)
        X.append(x)
        A.append(a)
    #print(N, T, X, A)
    #init
    ans = 0
    #search
    for i in range(N):
        if i == 0:
            ans += A[i]
            #print("i=0, ans=", ans)
        else:
            if T[i] - T[i-1] >= abs(X[i] - X[i-1]):
                ans += A[i]
                #print("i=",i, ", ans=", ans)
    #output
    print(ans)
    return
