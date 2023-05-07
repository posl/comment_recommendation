def main():
    S = [input() for _ in range(9)]
    ans = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == '#':
                for x in range(9):
                    for y in range(9):
                        if S[x][y] == '#':
                            for z in range(9):
                                for w in range(9):
                                    if S[z][w] == '#':
                                        for a in range(9):
                                            for b in range(9):
                                                if S[a][b] == '#':
                                                    if i == x == z == a and j < y < w < b:
                                                        ans += 1
                                                    if i == x == a == z and j < w < y < b:
                                                        ans += 1
                                                    if i == z == a == x and j < y < b < w:
                                                        ans += 1
                                                    if i == z == x == a and j < b < y < w:
                                                        ans += 1
                                                    if j == y == w == b and i < x < z < a:
                                                        ans += 1
                                                    if j == y == b == w and i < z < x < a:
                                                        ans += 1
                                                    if j == w == b == y and i < x < a < z:
                                                        ans += 1
                                                    if j == w == y == b and i < a < x < z:
                                                        ans += 1
                                                    if i == x == z == a and j < y < w < b:
                                                        ans += 1
                                                    if i == x == a == z and j < w < y < b:
                                                        ans += 1
                                                    if i == z == a == x and j < y < b < w:
                                                        ans += 1
                                                    if i == z == x == a and j < b < y < w:
                                                        ans += 1
                                                    if j == y == w == b and i < x < z < a:
                                                        ans += 1
                                                    if j == y == b == w and i < z < x < a:
                                                        ans += 1
                                                    if j == w == b == y and i < x < a < z:
                                                        ans += 1
                                                    if j == w == y == b and i < a < x

if __name__ == '__main__':
    main()