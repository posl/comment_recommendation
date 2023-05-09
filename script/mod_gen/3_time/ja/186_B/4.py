def main():
    h, w = map(int, input().split())
    a = []
    for _ in range(h):
        a.append(list(map(int, input().split())))
    min_a = 100
    for i in range(h):
        for j in range(w):
            min_a = min(min_a, a[i][j])
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_a
    print(ans)

if __name__ == '__main__':
    main()