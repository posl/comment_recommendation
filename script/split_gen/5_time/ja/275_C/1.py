def main():
    S = []
    for i in range(9):
        S.append(input())
    ans = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == "#":
                ans += 1
    print(ans)
