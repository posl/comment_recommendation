def solve():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    min = 100000
    res = 0
    for i in range(len(h)):
        if abs(t - h[i] * 0.006 - a) < min:
            min = abs(t - h[i] * 0.006 - a)
            res = i + 1
    print(res)

if __name__ == '__main__':
    solve()