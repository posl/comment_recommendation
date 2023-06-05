def solve(n,m,ss):
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            ok = True
            for k in range(m):
                if ss[i][k] == 'x' and ss[j][k] == 'x':
                    ok = False
            if ok:
                ans += 1
    return ans

if __name__ == '__main__':
    solve()