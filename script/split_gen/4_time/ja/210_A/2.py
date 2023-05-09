def main():
    n, a, x, y = map(int, input().split())
    ans = 0
    if n <= a:
        ans = n * x
    else:
        ans = a * x + (n - a) * y
    print(ans)
