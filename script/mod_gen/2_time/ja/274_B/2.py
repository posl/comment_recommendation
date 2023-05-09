def main():
    h,w = map(int,input().split())
    c = [list(input()) for _ in range(h)]
    ans = [0] * w
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                ans[j] += 1
    print(*ans)

if __name__ == '__main__':
    main()