def solve(n, a):
    if sum(a) % n != 0:
        return -1
    target = sum(a) // n
    cnt = 0
    for i in range(n):
        if a[i] % 2 == 0:
            while a[i] % 2 == 0:
                a[i] //= 2
                cnt += 1
        if a[i] % 3 == 0:
            while a[i] % 3 == 0:
                a[i] //= 3
                cnt += 1
    return cnt
n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))
