def main():
    n, l = map(int, input().split())
    ans = 0
    for i in range(n):
        ans += l + i
    if l > 0:
        ans -= l
    elif l + n - 1 < 0:
        ans -= l + n - 1
    print(ans)
