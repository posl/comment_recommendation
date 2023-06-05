def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(k):
        ans += a[i]
        if ans >= n:
            print(ans - n)
            return
        ans *= 2
    print(ans + 1 - n)
