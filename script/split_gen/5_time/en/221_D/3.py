def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.sort()
    b.sort()
    if n % 2 == 0:
        ans = b[n // 2] + b[n // 2 - 1] - a[n // 2] - a[n // 2 - 1] + 1
    else:
        ans = b[n // 2] - a[n // 2] + 1
    print(ans)
