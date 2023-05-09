def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(h)]
    b = [[0] * h for i in range(w)]
    for i in range(h):
        for j in range(w):
            b[j][i] = a[i][j]
    for i in range(w):
        print(*b[i])

if __name__ == '__main__':
    main()