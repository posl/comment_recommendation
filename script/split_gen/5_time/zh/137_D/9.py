def main():
    n, m = map(int, input().split())
    works = []
    for _ in range(n):
        a, b = map(int, input().split())
        works.append((a, b))
    works.sort(key=lambda x: x[0])
    ans = 0
    for a, b in works:
        if m >= a:
            m -= a
            ans += b
    print(ans)
