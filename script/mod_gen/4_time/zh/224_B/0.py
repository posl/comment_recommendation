def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    for i1 in range(h):
        for j1 in range(w):
            for i2 in range(i1+1, h):
                for j2 in range(j1+1, w):
                    if a[i1][j1] + a[i2][j2] > a[i1][j2] + a[i2][j1]:
                        print('No')
                        return
    print('Yes')

if __name__ == '__main__':
    main()