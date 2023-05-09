def main():
    a, n = map(int, input().split())
    x = 1
    ans = 0
    while x < n:
        ans += 1
        x = x * a
    print(ans)
