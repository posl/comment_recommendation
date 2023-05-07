def main():
    a, b = map(int, input().split())
    ans = 1000000000000000000
    for i in range(1000000):
        ans = min(ans, i + a / (i + 1) ** 0.5)
    print(ans)
