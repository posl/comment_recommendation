def main():
    h, w = map(int, input().split())
    c = [input() for _ in range(h)]
    x = [0] * w
    for j in range(w):
        for i in range(h):
            if c[i][j] == '#':
                x[j] += 1
    print(' '.join(map(str, x)))

if __name__ == '__main__':
    main()