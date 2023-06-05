def solve(n,x,y):
    ans = [0 for i in range(n)]
    for i in range(1,n):
        for j in range(i+1,n+1):
            d = min(j-i,abs(x-i)+1+abs(y-j),abs(y-i)+1+abs(x-j))
            ans[d] += 1
    for i in range(1,n):
        print(ans[i])

if __name__ == '__main__':
    solve()