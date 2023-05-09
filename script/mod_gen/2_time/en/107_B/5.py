def main():
    H, W = map(int, input().split())
    a = [input() for i in range(H)]
    b = [[a[i][j] for i in range(H)] for j in range(W)]
    a = ["".join(i) for i in a if i.count("#") > 0]
    b = ["".join(i) for i in b if i.count("#") > 0]
    for i in a:
        print(i)
    for i in b:
        print(i)

if __name__ == '__main__':
    main()