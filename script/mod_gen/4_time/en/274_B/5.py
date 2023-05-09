def main():
    h, w = map(int, input().split())
    c = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(h):
        c[i] = input()
    for i in range(w):
        x = 0
        for j in range(h):
            if c[j][i] == '#':
                x += 1
        print(x)

if __name__ == '__main__':
    main()