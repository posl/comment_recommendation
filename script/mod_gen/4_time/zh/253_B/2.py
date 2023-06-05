def main():
    h, w = map(int, input().split())
    s = [input() for i in range(h)]
    for i in range(h):
        for j in range(w):
            if s[i][j] == 'o':
                start = [i, j]
    result = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == 'o':
                result = max(result, abs(i - start[0]) + abs(j - start[1]))
    print(result)

if __name__ == '__main__':
    main()