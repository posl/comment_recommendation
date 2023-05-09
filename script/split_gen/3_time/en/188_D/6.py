def main():
    n, c = map(int, input().split())
    abcs = [list(map(int, input().split())) for _ in range(n)]
    abcs.sort()
    ans = 0
    t = 0
    for abc in abcs:
        a, b, c = abc
        t += (a - t) * c
        ans += (b - a + 1) * c
    print(ans + (c - t))
