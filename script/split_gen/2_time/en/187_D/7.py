def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    c = []
    for i in range(n):
        c.append(a[i] + b[i])
    c.sort(reverse = True)
    ans = 0
    s = 0
    for i in range(n):
        s += c[i]
        ans += 1
        if s > sum(a):
            break
    print(ans)
