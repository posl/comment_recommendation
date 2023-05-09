def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    s = 0
    for i in range(n):
        s += a[i]
        ans = max(ans, s)
        if s < 0:
            s = 0
    print(ans)
