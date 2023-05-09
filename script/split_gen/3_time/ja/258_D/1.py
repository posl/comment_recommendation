def main():
    n, x = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    ans = 10 ** 18
    for i in range(n):
        ans = min(ans, a[i] * x + b[i] * (n - 1 - i))
    print(ans)
