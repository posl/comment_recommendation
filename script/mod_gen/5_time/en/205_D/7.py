def solve(n, q, a, k):
    ret = []
    for i in k:
        ret.append(find_kth(a, i))
    return ret

if __name__ == '__main__':
    solve()