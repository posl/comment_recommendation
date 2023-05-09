def main():
    S = [input() for _ in range(9)]
    ans = 0
    for i in range(9):
        for j in range(9):
            for k in range(9):
                for l in range(9):
                    if i == k or j == l or abs(i-k) == abs(j-l):
                        continue
                    if S[i][j] == '#' and S[k][l] == '#' and S[i][l] == '#' and S[k][j] == '#':
                        ans += 1
    print(ans//4)
