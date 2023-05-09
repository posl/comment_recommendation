def main():
    n, m = map(int, input().split())
    ab = []
    for i in range(n):
        a, b = map(int, input().split())
        ab.append((a, b))
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
