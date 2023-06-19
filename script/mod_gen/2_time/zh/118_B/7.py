def main():
    n,m = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(n)]
    b = [0] * m
    for i in range(n):
        for j in range(1, a[i][0]+1):
            b[a[i][j]-1] += 1
    print(b.count(n))

if __name__ == '__main__':
    main()