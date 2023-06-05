def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    min_n = min(map(min, a))
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_n
    print(ans)

if __name__ == '__main__':
    main()