def main():
    n, m = map(int, input().split())
    k = [0] * n
    a = [0] * n
    for i in range(n):
        k[i], *a[i] = map(int, input().split())
    #print(k)
    #print(a)
    like = [0] * m
    for i in range(n):
        for j in range(k[i]):
            like[a[i][j] - 1] += 1
    #print(like)
    count = 0
    for i in range(m):
        if like[i] == n:
            count += 1
    print(count)

if __name__ == '__main__':
    main()