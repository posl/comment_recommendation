def solve(n, a):
    ans = 0
    for i in range(n):
        if a[i] > i+1:
            continue
        if i+1 < a[a[i]-1]:
            continue
        if i+1 == a[a[i]-1]:
            ans += 1
    return ans

if __name__ == '__main__':
    solve()