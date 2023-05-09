def solve(a,b,k):
    if k <= a:
        return (a-k,b)
    elif k <= a+b:
        return (0,a+b-k)
    elif k > a+b:
        return (0,0)
a,b,k = map(int,input().split())
ans = solve(a,b,k)
print(ans[0],ans[1])

if __name__ == '__main__':
    solve()