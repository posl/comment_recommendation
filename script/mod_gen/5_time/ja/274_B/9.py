def main():
    h, w = map(int, input().split())
    c = [input() for _ in range(h)]
    for i in range(h):
        cnt = 0
        for j in range(w):
            if c[i][j] == '#':
                cnt += 1
        print(cnt)

if __name__ == '__main__':
    main()