def main():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    t = [list(input()) for _ in range(h)]
    for i in range(h):
        s[i].sort()
        t[i].sort()
    for i in range(h):
        for j in range(w):
            if s[i][j] != t[i][j]:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()