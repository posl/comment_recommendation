def main():
    n = int(input())
    a, b = [], []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    ans = 0
    for i in range(n):
        ans += min(a[i], b[i])
    print(ans)
    return
