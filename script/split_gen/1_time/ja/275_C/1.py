def main():
    S = []
    for i in range(9):
        S.append(input())
    count = 0
    for i in range(7):
        for j in range(7):
            if S[i][j] == "#" and S[i][j+1] == "#" and S[i+1][j] == "#" and S[i+1][j+1] == "#":
                count += 1
    print(count)
