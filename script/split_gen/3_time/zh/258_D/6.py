def main():
    n, x = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0])
    ans = 0
    for a, b in ab:
        ans += a + b
    ans += x * ab[-1][0]
    print(ans)
