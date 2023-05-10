def main():
    h,w = map(int,input().split())
    s = [list(input()) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "o":
                cnt += 1
    if cnt == 1:
        print(0)
        exit()
    for i in range(h):
        for j in range(w):
            if s[i][j] == "o":
                if i-1 >= 0:
                    if s[i-1][j] == "-":
                        s[i-1][j] = "o"
                        s[i][j] = "-"
                        cnt += 1
                if i+1 < h:
                    if s[i+1][j] == "-":
                        s[i+1][j] = "o"
                        s[i][j] = "-"
                        cnt += 1
                if j-1 >= 0:
                    if s[i][j-1] == "-":
                        s[i][j-1] = "o"
                        s[i][j] = "-"
                        cnt += 1
                if j+1 < w:
                    if s[i][j+1] == "-":
                        s[i][j+1] = "o"
                        s[i][j] = "-"
                        cnt += 1
    print(cnt)
