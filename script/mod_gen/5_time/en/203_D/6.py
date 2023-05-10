def main():
    n, k = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    a.sort()
    a = list(zip(*a))
    a.sort()
    a = list(zip(*a))
    ans = 10**9
    for i in range(n-k+1):
        for j in range(n-k+1):
            ans = min(ans, a[i+k-1][j+k-1])
    print(ans)

if __name__ == '__main__':
    main()