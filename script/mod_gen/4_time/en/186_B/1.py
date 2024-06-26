def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    min_a = min([min(row) for row in a])
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_a
    print(ans)

if __name__ == '__main__':
    main()