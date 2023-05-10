def solve():
    N = int(input())
    A = list(map(int, input().split()))
    d = {}
    for a in A:
        if a in d:
            d[a] += 1
        else:
            d[a] = 1
    ret = 0
    for a in d:
        ret += d[a] * (d[a] - 1) // 2
    print(ret)

if __name__ == '__main__':
    solve()