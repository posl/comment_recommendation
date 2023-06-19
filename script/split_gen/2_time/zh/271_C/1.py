def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(0)
        return
    if n == 2:
        print(1)
        return
    a.sort()
    ans = 0
    for i in range(n):
        if i == 0:
            ans += 1
        elif a[i] != a[i-1]:
            ans += 1
    print(ans)
