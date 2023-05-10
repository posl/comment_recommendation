def main():
    n = int(input())
    s = [input() for _ in range(n)]
    # check if 6 or more consecutive squares are painted black aligned vertically or horizontally
    for i in range(n):
        for j in range(n):
            if j+5 < n:
                if s[i][j:j+6] == "######":
                    print("Yes")
                    return
            if i+5 < n:
                if s[i][j] == "#" and s[i+1][j] == "#" and s[i+2][j] == "#" and s[i+3][j] == "#" and s[i+4][j] == "#" and s[i+5][j] == "#":
                    print("Yes")
                    return
    # check if 6 or more consecutive squares are painted black aligned diagonally
    for i in range(n):
        for j in range(n):
            if i+5 < n and j+5 < n:
                if s[i][j] == "#" and s[i+1][j+1] == "#" and s[i+2][j+2] == "#" and s[i+3][j+3] == "#" and s[i+4][j+4] == "#" and s[i+5][j+5] == "#":
                    print("Yes")
                    return
            if i+5 < n and j-5 >= 0:
                if s[i][j] == "#" and s[i+1][j-1] == "#" and s[i+2][j-2] == "#" and s[i+3][j-3] == "#" and s[i+4][j-4] == "#" and s[i+5][j-5] == "#":
                    print("Yes")
                    return
    print("No")
