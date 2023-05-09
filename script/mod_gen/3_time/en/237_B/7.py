def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    b = [list(x) for x in zip(*a)]
    for i in range(w):
        for j in range(h):
            print(b[i][j], end=' ')
        print()

if __name__ == '__main__':
    main()