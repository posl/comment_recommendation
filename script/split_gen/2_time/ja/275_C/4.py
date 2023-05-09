def solve():
    S = [input() for _ in range(9)]
    ans = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == ".":
                continue
            for k in range(9):
                for l in range(9):
                    if S[k][l] == ".":
                        continue
                    for m in range(9):
                        for n in range(9):
                            if S[m][n] == ".":
                                continue
                            for o in range(9):
                                for p in range(9):
                                    if S[o][p] == ".":
                                        continue
                                    if i == k == m == o and j < l < n < p:
                                        ans += 1
                                    if i == k == o == m and j < l < p < n:
                                        ans += 1
                                    if i == m == o == k and j < n < p < l:
                                        ans += 1
                                    if k == m == o == i and l < n < p < j:
                                        ans += 1
                                    if i == k == m == o and j > l > n > p:
                                        ans += 1
                                    if i == k == o == m and j > l > p > n:
                                        ans += 1
                                    if i == m == o == k and j > n > p > l:
                                        ans += 1
                                    if k == m == o == i and l > n > p > j:
                                        ans += 1
    print(ans // 8)
