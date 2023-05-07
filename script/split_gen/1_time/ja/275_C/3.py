def main():
    S = [input() for _ in range(9)]
    ans = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == '#':
                for k in range(9):
                    if S[i][k] == '.' or S[k][j] == '.':
                        break
                else:
                    ans += 1
    print(ans)
