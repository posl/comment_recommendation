def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        for i in range(n):
            if a[i] % 2 != 0 and a[i] % 3 != 0:
                print(-1)
                return
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] //= 2
        ans += 1
        if all(a[0] == x for x in a):
            print(ans)
            return
