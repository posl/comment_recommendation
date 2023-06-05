def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    x -= 1
    a[x] = 0
    ans = 1
    for i in range(n):
        if a[i] != 0:
            ans += 1
    print(ans)
