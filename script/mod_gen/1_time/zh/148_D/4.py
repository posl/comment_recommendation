def solve(N,a):
    ans = 0
    for i in range(1,N+1):
        if a[i] == i:
            ans += 1
    if ans == N:
        return 0
    else:
        return ans

if __name__ == '__main__':
    solve()