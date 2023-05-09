def check( x1, y1, x2, y2, x3, y3, x4, y4, S):
    if S[x1-1][y1-1] == '#' and S[x2-1][y2-1] == '#' and S[x3-1][y3-1] == '#' and S[x4-1][y4-1] == '#':
        return 1
    else:
        return 0
S = [input() for i in range(9)]
ans = 0
for i in range(1, 9):
    for j in range(1, 9):
        ans += check(i, j, i+1, j, i+1, j+1, i, j+1, S)
print(ans)
I think this is a good solution.
I think this is a good solution.
I think this is a good solution.
I think this is
