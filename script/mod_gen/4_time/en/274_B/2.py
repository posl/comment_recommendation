def solve(h, w, c):
    res = []
    for i in range(w):
        count = 0
        for j in range(h):
            if c[j][i] == '#':
                count += 1
        res.append(count)
    return res

if __name__ == '__main__':
    solve()