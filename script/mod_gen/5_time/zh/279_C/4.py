def main():
    h,w = map(int,input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    s_col = [0]*w
    s_row = [0]*h
    t_col = [0]*w
    t_row = [0]*h
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                s_col[j] += 1
                s_row[i] += 1
            if t[i][j] == '#':
                t_col[j] += 1
                t_row[i] += 1
    if s_col == t_col and s_row == t_row:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()