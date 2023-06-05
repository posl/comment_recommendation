def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    for i in range(w):
        for j in range(h):
            if j == h - 1:
                print(a[j][i])
            else:
                print(a[j][i], end=' ')

if __name__ == '__main__':
    main()