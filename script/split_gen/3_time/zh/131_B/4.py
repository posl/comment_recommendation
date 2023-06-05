def main():
    n, l = map(int, input().split())
    l += 1
    ans = 0
    for i in range(1, n):
        ans += l + i - 1
    print(ans)
