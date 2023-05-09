def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if s[i][j] == "o":
                x, y = i, j
    print(max(x, h-x-1) + max(y, w-y-1))

if __name__ == '__main__':
    main()