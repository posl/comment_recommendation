def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = {}
    for i in range(n):
        if a[i] not in c:
            c[a[i]] = 1
        else:
            c[a[i]] += 1
    ans = 0
    for i in c:
        ans += c[i] - 1
    print(ans)
