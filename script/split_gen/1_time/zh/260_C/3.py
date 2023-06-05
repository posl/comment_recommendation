def main():
    n,x,y = map(int,input().split())
    ans = 0
    for i in range(1,n):
        if i <= x:
            ans += (n-i)*x+1-i
        else:
            ans += y*(n-i)+1-i
    print(ans)
