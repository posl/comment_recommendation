def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            for k in range(h):
                for l in range(w):
                    if i != k and j != l:
                        if a[i][j] + a[k][l] > a[k][j] + a[i][l]:
                            print('No')
                            return
    print('Yes')

if __name__ == '__main__':
    main()