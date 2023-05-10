def solve():
    n, m = map(int, input().split())
    k = [0] * m
    a = [[] for _ in range(m)]
    for i in range(m):
        k[i] = int(input())
        a[i] = list(map(int, input().split()))
    for i in range(m):
        if k[i] % 2 == 1:
            return 'No'
    for i in range(m):
        for j in range(k[i]):
            x = a[i][j]
            for l in range(i+1, m):
                if x in a[l]:
                    return 'No'
    return 'Yes'
print(solve())

if __name__ == '__main__':
    solve()