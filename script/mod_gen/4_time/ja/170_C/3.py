def solve():
    x, n = map(int, input().split())
    if n == 0:
        return x
    p = list(map(int, input().split()))
    p.sort()
    if x not in p:
        return x
    for i in range(1, 100):
        if x - i not in p:
            return x - i
        elif x + i not in p:
            return x + i

if __name__ == '__main__':
    solve()