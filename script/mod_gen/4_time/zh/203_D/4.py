def main():
    n, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = float('inf')
    for i in range(n-k+1):
        for j in range(n-k+1):
            b = []
            for x in range(i, i+k):
                for y in range(j, j+k):
                    b.append(a[x][y])
            b.sort()
            ans = min(ans, b[k*k//2])
    print(ans)

if __name__ == '__main__':
    main()