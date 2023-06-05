def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    a.sort(reverse=True)
    b.sort(reverse=True)
    ans = 0
    for i in range(n):
        ans += a[i] * i + b[i] * (n - i - 1)
    print(ans)
