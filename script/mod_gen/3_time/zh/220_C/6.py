def solve():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    a_sum = sum(a)
    k = x // a_sum * n
    x %= a_sum
    for i in range(n):
        if x < 0:
            break
        x -= a[i]
        k += 1
    print(k)
solve()
