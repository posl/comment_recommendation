def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    ans = 10**10
    for i in range(n):
        for j in range(n):
            if i == j:
                ans = min(ans, a[i]+b[i])
            else:
                ans = min(ans, max(a[i], b[j]))
    print(ans)
