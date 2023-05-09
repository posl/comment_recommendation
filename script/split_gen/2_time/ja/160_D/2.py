def main():
    import sys
    input = sys.stdin.readline
    N,X,Y = map(int,input().split())
    X,Y = X-1,Y-1
    ans = [0]*(N-1)
    for i in range(N-1):
        for j in range(i+1,N):
            k = min(j-i,abs(X-i)+1+abs(j-Y),abs(Y-j)+1+abs(i-X))
            ans[k-1] += 1
    for i in range(N-1):
        print(ans[i])
