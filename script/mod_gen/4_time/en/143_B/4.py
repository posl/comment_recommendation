def solve():
    n = int(input())
    d = list(map(int, input().split()))
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            res += d[i] * d[j]
    print(res)

if __name__ == '__main__':
    solve()