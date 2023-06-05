def main():
    n,m = map(int,input().split())
    b = []
    for i in range(n):
        b.append(list(map(int,input().split())))
    b = list(map(list,zip(*b)))
    for i in range(n):
        for j in range(m):
            b[i][j] -= i * 7
    for i in range(n):
        for j in range(1,m):
            if b[i][j] != b[i][j-1] + 1:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()