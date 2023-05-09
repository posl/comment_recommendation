def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    #print(s)
    #print("h = ", h, "w = ", w)
    side = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                #print("i = ", i, "j = ", j)
                if i == 0 or j == 0 or i == h - 1 or j == w - 1:
                    side = 4
                elif s[i - 1][j] == "#" or s[i + 1][j] == "#" or s[i][j - 1] == "#" or s[i][j + 1] == "#":
                    side = 4
                else:
                    side = 8
                    break
        if side == 8:
            break
    print(side)
main()
