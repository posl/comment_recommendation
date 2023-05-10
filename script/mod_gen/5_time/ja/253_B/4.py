def main():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "o":
                ans += 1
    if ans == 1:
        print(0)
        exit()
    for i in range(h):
        for j in range(w):
            if s[i][j] == "o":
                if i-1 >= 0 and s[i-1][j] == "o":
                    ans -= 1
                if i+1 < h and s[i+1][j] == "o":
                    ans -= 1
                if j-1 >= 0 and s[i][j-1] == "o":
                    ans -= 1
                if j+1 < w and s[i][j+1] == "o":
                    ans -= 1
    print(ans)

if __name__ == '__main__':
    main()