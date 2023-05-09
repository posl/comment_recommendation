def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if s[i][j] == 'o':
                a = i
                b = j
    for i in range(h):
        for j in range(w):
            if s[i][j] == 'o':
                c = i
                d = j
    print(max(abs(a-c), abs(b-d)))

if __name__ == '__main__':
    main()