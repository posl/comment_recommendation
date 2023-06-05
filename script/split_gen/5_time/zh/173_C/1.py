def solve(h, w, k, c):
    ans = 0
    for i in range(2**h):
        for j in range(2**w):
            cnt = 0
            for k1 in range(h):
                for l1 in range(w):
                    if (i >> k1) & 1 == 0 and (j >> l1) & 1 == 0 and c[k1][l1] == '#':
                        cnt += 1
            if cnt == k:
                ans += 1
    return ans
