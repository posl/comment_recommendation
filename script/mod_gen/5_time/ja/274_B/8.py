def main():
    h, w = map(int, input().split())
    c = [list(input()) for i in range(h)]
    x = [0] * w
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                x[j] += 1
    for i in range(w):
        print(x[i], end=' ')
    print()

if __name__ == '__main__':
    main()