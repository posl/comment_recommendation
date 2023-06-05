def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    print(a)
    print(b)
    ans = 0
    for i in range(m):
        if a[i] == 1 or b[i] == n:
            ans += 1
    print(ans)
