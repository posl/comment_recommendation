def solve(h, w, a):
    ans = 0
    for i in range(h):
        ans += sum(a[i])
    ans -= h * w * min([min(a[i]) for i in range(h)])
    return ans

if __name__ == '__main__':
    solve()