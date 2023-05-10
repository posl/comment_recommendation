def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    for i in range(w):
        cnt = 0
        for j in range(h):
            if a[j][i] == '#':
                cnt += 1
        print(cnt)

if __name__ == '__main__':
    main()