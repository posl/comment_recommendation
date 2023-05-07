def main():
    n,x,y = map(int,input().split())
    ans = [0]*(n-1)
    for i in range(1,n):
        for j in range(i+1,n+1):
            #print(i,j)
            d = min(j-i,abs(x-i)+1+abs(y-j),abs(y-i)+1+abs(x-j))
            #print(d)
            ans[d-1] += 1
    for i in range(n-1):
        print(ans[i])
    return
