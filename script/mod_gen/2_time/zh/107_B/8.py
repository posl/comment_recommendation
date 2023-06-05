def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    h_list = [0 for _ in range(h)]
    w_list = [0 for _ in range(w)]
    for i in range(h):
        for j in range(w):
            if a[i][j] == '#':
                h_list[i] = 1
                w_list[j] = 1
    for i in range(h):
        if h_list[i] == 1:
            for j in range(w):
                if w_list[j] == 1:
                    print(a[i][j], end='')
            print()

if __name__ == '__main__':
    main()