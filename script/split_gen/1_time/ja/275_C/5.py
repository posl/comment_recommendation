def main():
    S = []
    for i in range(9):
        S.append(list(input()))
    
    ans = 0
    for i in range(9):
        for j in range(9):
            for k in range(9):
                for l in range(9):
                    if i == k and j == l:
                        continue
                    if i == k or j == l:
                        continue
                    if abs(i - k) == abs(j - l):
                        continue
                    if S[i][j] == "#" and S[k][l] == "#":
                        x1 = min(i, k)
                        x2 = max(i, k)
                        y1 = min(j, l)
                        y2 = max(j, l)
                        if x2 - x1 == y2 - y1:
                            if S[x1][y1] == "#" and S[x2][y2] == "#":
                                ans += 1
    print(ans//2)
