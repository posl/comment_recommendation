def solve(n, m, ab):
    ab.sort()
    ab.reverse()
    ab = ab[:m]
    ab.sort(key=lambda x: x[1])
    ab.reverse()
    return sum(map(lambda x: x[1], ab))
n, m = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(n)]
print(solve(n, m, ab))
