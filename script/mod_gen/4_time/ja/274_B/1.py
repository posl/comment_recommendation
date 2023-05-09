def main():
    h, w = map(int, input().split())
    c = [input() for _ in range(h)]
    x = [0] * w
    for i in range(w):
        for j in range(h):
            if c[j][i] == '#':
                x[i] += 1
    print(' '.join(map(str, x)))

if __name__ == '__main__':
    main()