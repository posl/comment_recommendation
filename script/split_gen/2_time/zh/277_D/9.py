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
    ans = 0
    for i in range(n):
        if a[i] > b[i]:
            ans = a[i]
            break
        elif i == n - 1:
            ans = b[-1] + 1
    print(ans)
