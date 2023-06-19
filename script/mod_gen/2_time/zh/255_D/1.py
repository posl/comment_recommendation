def solve(n, q, a, x):
    a.sort()
    x.sort()
    sum_a = sum(a)
    sum_x = sum(x)
    res = sum_x
    for i in range(q):
        res += n * x[i]
        sum_a += x[i]
        if res > sum_a:
            res = sum_a
        else:
            break
    return res

if __name__ == '__main__':
    solve()