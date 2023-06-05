def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    s_count = [0] * h
    t_count = [0] * h
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                s_count[i] += 1
            if t[i][j] == '#':
                t_count[i] += 1
    if s_count == t_count:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()