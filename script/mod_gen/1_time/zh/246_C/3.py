def solve(n, k, x, a):
    cost = 0
    for i in range(n):
        if k > 0:
            cost += max(a[i]-x, 0)
            k -= 1
        else:
            cost += a[i]
    return cost

if __name__ == '__main__':
    solve()