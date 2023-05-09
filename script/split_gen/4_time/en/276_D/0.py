def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        while a[i] % 2 == 0:
            ans += 1
            a[i] //= 2
        while a[i] % 3 == 0:
            ans += 1
            a[i] //= 3
    print(ans if len(set(a)) == 1 else -1)
