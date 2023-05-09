def main():
    S = []
    for i in range(9):
        S.append(input())
    cnt = 0
    for i in range(8):
        for j in range(8):
            if S[i][j] == "#" and S[i][j+1] == "#" and S[i+1][j] == "#" and S[i+1][j+1] == "#":
                cnt += 1
    print(cnt)
