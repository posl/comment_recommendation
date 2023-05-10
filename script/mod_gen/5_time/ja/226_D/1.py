def solve():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    ans = 0
    for i in range(n-1):
        for j in range(i+1,n):
            dx = x[i] - x[j]
            dy = y[i] - y[j]
            cnt = 0
            for k in range(n):
                for l in range(n):
                    if x[k] - x[l] == dx and y[k] - y[l] == dy:
                        cnt += 1
            ans = max(ans,cnt)
    print(n-ans)
    return 0

if __name__ == '__main__':
    solve()