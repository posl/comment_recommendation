def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                count += 1
    print(count)

if __name__ == '__main__':
    main()