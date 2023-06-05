def solve():
    n = int(input())
    a = list(map(int, input().split()))
    minus_cnt = 0
    min_abs = 10**9
    sum = 0
    for i in range(n):
        if a[i] < 0:
            minus_cnt += 1
        abs_a = abs(a[i])
        if min_abs > abs_a:
            min_abs = abs_a
        sum += abs_a
    if minus_cnt % 2 == 0:
        print(sum)
    else:
        print(sum - min_abs * 2)
solve()
