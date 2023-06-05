def main():
    N,X,Y = map(int,input().split())
    ans = [0 for i in range(N)]
    for i in range(1,N):
        for j in range(i+1,N+1):
            ans[min(j-i,abs(X-i)+abs(Y-j)+1)] += 1
    for i in range(1,N):
        print(ans[i])
