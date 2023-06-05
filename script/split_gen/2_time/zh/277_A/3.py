def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] //= 2
            ans += 1
        while a[i] % 3 == 0:
            a[i] //= 3
            ans += 1
    if len(set(a)) == 1:
        print(ans)
    else:
        print(-1)
