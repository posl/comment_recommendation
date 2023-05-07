def main():
    n, m = map(int, input().split())
    cake = []
    for i in range(n):
        cake.append(list(map(int, input().split())))
    ans = 0
    for i in range(8):
        cake.sort(key = lambda x: sum([(-1)**((i>>j)&1)*x[j] for j in range(3)]), reverse = True)
        ans = max(ans, sum([sum([(-1)**((i>>j)&1)*cake[k][j] for j in range(3)]) for k in range(m)]))
    print(ans)

if __name__ == '__main__':
    main()