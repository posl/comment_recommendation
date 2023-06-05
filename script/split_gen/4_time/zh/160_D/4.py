def main():
    n,x,y = map(int,input().split())
    x-=1
    y-=1
    ans = [0 for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            d = min(j-i,abs(x-i)+abs(y-j)+1)
            ans[d] += 1
    for i in range(1,n):
        print(ans[i])
