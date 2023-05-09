def main():
    n = int(input())
    s = [input() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if s[i][j] == "#":
                continue
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if ni >= 0 and ni < n and nj >= 0 and nj < n and s[ni][nj] == "#":
                    for l in range(4):
                        ni2 = ni + di[l]
                        nj2 = nj + dj[l]
                        if ni2 >= 0 and ni2 < n and nj2 >= 0 and nj2 < n and s[ni2][nj2] == "#":
                            for m in range(4):
                                ni3 = ni2 + di[m]
                                nj3 = nj2 + dj[m]
                                if ni3 >= 0 and ni3 < n and nj3 >= 0 and nj3 < n and s[ni3][nj3] == "#":
                                    print("Yes")
                                    return
    print("No")
