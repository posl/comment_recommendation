def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.sort(reverse=True)
    b.sort(reverse=True)
    ans = 0
    for i in range(n):
        ans += a[i] * i + b[i] * (n - i)
    print(ans)
