def main():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    t = [list(input()) for _ in range(h)]
    s = [sorted(x) for x in s]
    t = [sorted(x) for x in t]
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