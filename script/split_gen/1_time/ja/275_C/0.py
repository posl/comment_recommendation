def main():
    S = [input() for _ in range(9)]
    ans = 0
    for i in range(9):
        for j in range(9):
            for k in range(9):
                for l in range(9):
                    if i + k < 9 and j + l < 9:
                        if S[i][j] == '#' and S[i][j + l] == '#' and S[i + k][j] == '#' and S[i + k][j + l] == '#':
                            ans += 1
    print(ans)
