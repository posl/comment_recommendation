def main():
    h, w = map(int, input().split())
    c = [input() for _ in range(h)]
    for j in range(w):
        x = 0
        for i in range(h):
            if c[i][j] == '#':
                x += 1
        print(x, end=' ')
    print()

if __name__ == '__main__':
    main()