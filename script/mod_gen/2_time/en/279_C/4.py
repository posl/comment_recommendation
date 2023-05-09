def main():
    h, w = map(int, input().split())
    s = [input() for i in range(h)]
    t = [input() for i in range(h)]
    for i in range(h):
        s[i] = list(s[i])
        t[i] = list(t[i])
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                s[i][j] = 1
            else:
                s[i][j] = 0
            if t[i][j] == '#':
                t[i][j] = 1
            else:
                t[i][j] = 0
    for i in range(w):
        for j in range(i, w):
            s2 = [s[i][j] for i in range(h)]
            s2.sort()
            t2 = [t[i][j] for i in range(h)]
            t2.sort()
            if s2 == t2:
                for k in range(i + 1, w):
                    s2 = [s[i][k] for i in range(h)]
                    s2.sort()
                    t2 = [t[i][k] for i in range(h)]
                    t2.sort()
                    if s2 != t2:
                        print('No')
                        return
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    main()