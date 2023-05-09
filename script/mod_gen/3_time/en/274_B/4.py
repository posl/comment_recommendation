def main():
    h, w = map(int, input().split())
    c = [input() for _ in range(h)]
    for j in range(w):
        cnt = 0
        for i in range(h):
            if c[i][j] == '#':
                cnt += 1
        print(cnt, end=' ')
    print()

if __name__ == '__main__':
    main()