def main():
    N,X,Y = map(int,input().split())
    X -= 1
    Y -= 1
    ans = [0] * (N-1)
    for i in range(N):
        for j in range(i+1,N):
            d = min(j-i,abs(X-i)+1+abs(j-Y))
            ans[d-1] += 1
    for i in range(N-1):
        print(ans[i])
