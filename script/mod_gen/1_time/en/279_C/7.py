def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    s_ = []
    for i in range(h):
        temp = []
        for j in range(w):
            if s[i][j] == '#':
                temp.append(j)
        s_.append(temp)
    t_ = []
    for i in range(h):
        temp = []
        for j in range(w):
            if t[i][j] == '#':
                temp.append(j)
        t_.append(temp)
    s_.sort()
    t_.sort()
    if s_ == t_:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()