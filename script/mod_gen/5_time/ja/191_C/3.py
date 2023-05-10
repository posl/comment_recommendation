def main():
    h,w = map(int,input().split())
    s = [list(input()) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                cnt += 1
    if cnt == 0:
        print(0)
        exit()
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                if i-1 < 0 or s[i-1][j] == ".":
                    ans += 1
                if j-1 < 0 or s[i][j-1] == ".":
                    ans += 1
                if i+1 >= h or s[i+1][j] == ".":
                    ans += 1
                if j+1 >= w or s[i][j+1] == ".":
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()