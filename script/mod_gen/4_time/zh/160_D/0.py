def solve(n,x,y):
    ans = [0] * n
    for i in range(1,n):
        for j in range(i+1,n+1):
            ans[min(abs(i-j),abs(x-i)+1+abs(y-j),abs(x-j)+1+abs(y-i))] += 1
    return ans[1:]

if __name__ == '__main__':
    solve()