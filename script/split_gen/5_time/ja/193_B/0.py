def main():
    n = int(input())
    a = [0] * n
    p = [0] * n
    x = [0] * n
    for i in range(n):
        a[i], p[i], x[i] = map(int, input().split())
    ans = 10**9
    for i in range(n):
        if x[i] - a[i] > 0:
            ans = min(ans, p[i])
    print(ans if ans != 10**9 else -1)
