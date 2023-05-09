def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    ans = 0
    for i in range(n):
        ans += min(a[i], b[i])
    print(ans)
