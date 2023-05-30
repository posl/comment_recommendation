def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for _ in range(m):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a = sorted(a)
    b = sorted(b)
    ans = 0
    for i in range(m):
        if a[i] != a[i-1] and b[i] != b[i-1]:
            ans += 1
    print(ans)
main()
