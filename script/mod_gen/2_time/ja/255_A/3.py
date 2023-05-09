def main():
    r, c = map(int, input().split())
    a = []
    for i in range(r):
        a.append(list(map(int, input().split())))
    print(a[r-1][c-1])

if __name__ == '__main__':
    main()