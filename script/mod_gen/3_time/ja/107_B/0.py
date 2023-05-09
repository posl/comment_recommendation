def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    rows = [False]*h
    cols = [False]*w
    for i in range(h):
        for j in range(w):
            if a[i][j] == '#':
                rows[i] = True
                cols[j] = True
    for i in range(h):
        if rows[i]:
            for j in range(w):
                if cols[j]:
                    print(a[i][j], end='')
            print()

if __name__ == '__main__':
    main()