def solve():
    n = int(input())
    h = list(map(int, input().split()))
    res = h[0]
    for i in range(1, n):
        if h[i] > h[i-1]:
            res = h[i]
    print(res)

if __name__ == '__main__':
    solve()