def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    for j in range(w):
        print(sum(1 for i in range(h) if a[i][j] == '#'), end=' ')
    print()

if __name__ == '__main__':
    main()