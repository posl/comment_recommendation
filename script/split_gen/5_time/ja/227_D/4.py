def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = 0
    ans += a[0]
    ans += sum(a[1:k])
    print(ans)
