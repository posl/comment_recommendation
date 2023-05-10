def main():
    n, k = map(int, input().split())
    a = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    ans = 10**9
    for i in range(n-k+1):
        for j in range(n-k+1):
            tmp = []
            for x in range(k):
                for y in range(k):
                    tmp.append(a[i+x][j+y])
            tmp.sort()
            ans = min(ans, tmp[k*k//2])
    print(ans)

if __name__ == '__main__':
    main()