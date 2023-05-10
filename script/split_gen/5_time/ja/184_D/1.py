def solve(a,b,c):
    table = [[[0 for i in range(100)] for j in range(100)] for k in range(100)]
    for i in range(99,-1,-1):
        for j in range(99,-1,-1):
            for k in range(99,-1,-1):
                if i+j+k == 0:
                    continue
                if i+j+k == 100:
                    continue
                table[i][j][k] = 1
                if i < 99:
                    table[i][j][k] += table[i+1][j][k] * i/(i+j+k)
                if j < 99:
                    table[i][j][k] += table[i][j+1][k] * j/(i+j+k)
                if k < 99:
                    table[i][j][k] += table[i][j][k+1] * k/(i+j+k)
    return table[a][b][c]
