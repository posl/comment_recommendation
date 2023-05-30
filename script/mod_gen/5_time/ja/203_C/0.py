def main():
    n, k = map(int, input().split())
    a, b = [], []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.append(0)
    b.append(0)
    a.sort()
    ans = k
    for i in range(n+1):
        if ans < a[i]:
            break
        ans += b[i]
    print(ans)
main()
