def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    ab.sort(key=lambda x: x[1])
    ans = 0
    last = 0
    for a, b in ab:
        if a > last:
            ans += 1
            last = b - 1
    print(ans)
