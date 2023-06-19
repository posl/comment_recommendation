def main():
    h,w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    min = a[0][0]
    for i in range(h):
        for j in range(w):
            if min > a[i][j]:
                min = a[i][j]
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min
    print(ans)

if __name__ == '__main__':
    main()