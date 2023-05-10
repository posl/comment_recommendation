def main():
    n,m = map(int,input().split())
    b = []
    for i in range(n):
        b.append(list(map(int,input().split())))
    for i in range(n):
        for j in range(m):
            b[i][j] -= 1
    for i in range(n):
        for j in range(m):
            if b[i][j] % 7 != j:
                print("No")
                return
    for i in range(n):
        for j in range(m):
            b[i][j] //= 7
    for i in range(n):
        for j in range(m):
            if b[i][j] != i:
                print("No")
                return
    print("Yes")
main()

if __name__ == '__main__':
    main()