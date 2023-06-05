def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    print(a)
    print(a[-k:])
    ans = 0
    for i in a[-k:]:
        ans += i
    print(ans)
