def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    s = [list(x) for x in s]
    t = [list(x) for x in t]
    s = sorted(s)
    t = sorted(t)
    for i in range(h):
        for j in range(w):
            if s[i][j] != t[i][j]:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()