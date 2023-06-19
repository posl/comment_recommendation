def main():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == ".":
                cnt = 0
                if i > 0 and s[i-1][j] == ".":
                    cnt += 1
                if i < h-1 and s[i+1][j] == ".":
                    cnt += 1
                if j > 0 and s[i][j-1] == ".":
                    cnt += 1
                if j < w-1 and s[i][j+1] == ".":
                    cnt += 1
                ans += 4 - cnt
    print(ans)
main()
