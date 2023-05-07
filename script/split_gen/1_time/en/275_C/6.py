def main():
    S = []
    for i in range(9):
        S.append(input())
    count = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == ".":
                continue
            if i + 2 < 9 and j + 2 < 9:
                if S[i][j] == "#" and S[i][j + 1] == "#" and S[i][j + 2] == "#" and S[i + 1][j] == "#" and S[i + 1][j + 2] == "#" and S[i + 2][j] == "#" and S[i + 2][j + 1] == "#" and S[i + 2][j + 2] == "#":
                    count += 1
    print(count)
