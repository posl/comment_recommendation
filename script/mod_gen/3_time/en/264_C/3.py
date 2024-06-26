def main():
    h1, w1 = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h1)]
    h2, w2 = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(h2)]
    if h1 < h2 or w1 < w2:
        print('No')
        return
    for i in range(h1 - h2 + 1):
        for j in range(w1 - w2 + 1):
            if all(a[i + k][j + l] == b[k][l] for k in range(h2) for l in range(w2)):
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    main()