def solve():
    s = []
    for i in range(9):
        s.append(input())
    ans = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == "#":
                if i >= 2 and j >= 2 and s[i-1][j-1] == "#" and s[i-2][j-2] == "#":
                    ans += 1
                if i >= 2 and s[i-1][j] == "#" and s[i-2][j] == "#":
                    ans += 1
                if i >= 2 and j <= 6 and s[i-1][j+1] == "#" and s[i-2][j+2] == "#":
                    ans += 1
                if j >= 2 and s[i][j-1] == "#" and s[i][j-2] == "#":
                    ans += 1
                if j <= 6 and s[i][j+1] == "#" and s[i][j+2] == "#":
                    ans += 1
                if i <= 6 and j >= 2 and s[i+1][j-1] == "#" and s[i+2][j-2] == "#":
                    ans += 1
                if i <= 6 and s[i+1][j] == "#" and s[i+2][j] == "#":
                    ans += 1
                if i <= 6 and j <= 6 and s[i+1][j+1] == "#" and s[i+2][j+2] == "#":
                    ans += 1
    print(ans)
solve()
