def main():
    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    min_a = [[float('inf')]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            min_a[i][j] = min(min_a[i-1][j], min_a[i][j-1]) + a[i][j]
    min_b = [[float('inf')]*w for _ in range(h)]
    for i in range(h-1, -1, -1):
        for j in range(w-1, -1, -1):
            min_b[i][j] = min(min_b[i+1][j], min_b[i][j+1]) + a[i][j]
    ans = float('inf')
    for i in range(h):
        for j in range(w):
            ans = min(ans, min_a[i][j] + min_b[i][j] - a[i][j])
    for i in range(h):
        for j in range(w):
            ans = min(ans, min_a[i][j] + min_b[i][j] - a[i][j] + c)
    print(ans)

if __name__ == '__main__':
    main()