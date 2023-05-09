def main():
    h, w, k = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    ans = 0
    for i in range(2 ** h):
        for j in range(2 ** w):
            cnt = 0
            for r in range(h):
                for c in range(w):
                    if i >> r & 1 or j >> c & 1:
                        continue
                    if grid[r][c] == '#':
                        cnt += 1
            if cnt == k:
                ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()