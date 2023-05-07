def main():
    N,X,Y = map(int,input().split())
    ans = [0] * N
    for i in range(1,N):
        for j in range(i+1,N+1):
            tmp = min(j-i,abs(i-X)+1+abs(j-Y))
            ans[tmp] += 1
    for i in range(1,N):
        print(ans[i])
