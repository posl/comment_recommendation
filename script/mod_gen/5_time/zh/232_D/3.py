def solve(h, w, s):
    #print(h, w, s)
    res = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue
            t = 0
            for k in range(i, h):
                if s[k][j] == '#':
                    break
                t += 1
            res = max(res, t)
            t = 0
            for k in range(j, w):
                if s[i][k] == '#':
                    break
                t += 1
            res = max(res, t)
    return res

if __name__ == '__main__':
    solve()