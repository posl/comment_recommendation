def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort()
    ans = 0
    for a, b in ab:
        if m > b:
            ans += a * b
            m -= b
        else:
            ans += a * m
            break
    print(ans)
