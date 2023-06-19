def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    i = 0
    while i < n:
        if i == n - 1:
            ans += 1
            i += 1
        elif a[i] == a[i + 1]:
            i += 2
        else:
            ans += 1
            i += 1
    print(ans)
