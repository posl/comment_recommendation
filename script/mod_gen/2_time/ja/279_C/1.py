def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    for i in range(h):
        s[i] = list(s[i])
        t[i] = list(t[i])
    s.sort()
    t.sort()
    for i in range(h):
        for j in range(w):
            if s[i][j] != t[i][j]:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()