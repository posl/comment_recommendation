def main():
    n, m = map(int, input().split())
    a = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        a[i] = list(map(int, input().split()))
    for i in range(m):
        for j in range(i+1, m):
            for k in range(n):
                if a[i][k] == a[j][k]:
                    print('Yes')
                    return
    print('No')
    return

if __name__ == '__main__':
    main()