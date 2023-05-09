def main():
    S = []
    for i in range(9):
        S.append(input())
    
    ans = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == "#":
                for k in range(9):
                    if i+k < 9 and j+k < 9 and S[i+k][j] == "#" and S[i][j+k] == "#" and S[i+k][j+k] == "#":
                        ans += 1
    print(ans)
