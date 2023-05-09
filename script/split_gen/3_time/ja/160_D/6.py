def main():
    N,X,Y = map(int,input().split())
    ans = [0 for i in range(N-1)]
    for i in range(1,N):
        for j in range(i+1,N+1):
            if i == X and j == Y:
                ans[min(j-i-1,N-j+i-1)] += 1
            else:
                ans[min(j-i-1,abs(X-i)+1+abs(Y-j))] += 1
    for i in range(N-1):
        print(ans[i])
