def main():
    h,w = map(int,input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue
            for k in range(4):
                ni = i + [1,0,-1,0][k]
                nj = j + [0,1,0,-1][k]
                if 0 <= ni < h and 0 <= nj < w and s[ni][nj] == '.':
                    ans += 1
    print(ans//2)

if __name__ == '__main__':
    main()