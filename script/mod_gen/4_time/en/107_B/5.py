def main():
    h, w = map(int, input().split())
    a = [list(input()) for _ in range(h)]
    for i in range(h):
        if a[i].count('.') == w:
            for j in range(w):
                a[i][j] = ''
    for j in range(w):
        if [a[i][j] for i in range(h)].count('') == h:
            for i in range(h):
                a[i][j] = ''
    for i in range(h):
        if a[i].count('') == w:
            continue
        else:
            print(''.join(a[i]))

if __name__ == '__main__':
    main()