def solve():
    n = int(input())
    a = list(map(int, input().split()))
    minus = 0
    abs_a = []
    for i in range(n):
        if a[i] < 0:
            minus += 1
        abs_a.append(abs(a[i]))
    if minus % 2 == 0:
        print(sum(abs_a))
    else:
        print(sum(abs_a) - 2 * min(abs_a))
