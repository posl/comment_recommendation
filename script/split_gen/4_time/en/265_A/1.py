def main():
    x, y, n = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        if i % 3 == 0:
            ans += y
        else:
            ans += x
    print(ans)
