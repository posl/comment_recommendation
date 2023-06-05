def solve():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    sum_a = sum(a)
    sum_b = sum_a * (10 ** (100 - 1))
    if sum_b <= x:
        print(10 ** 100)
        return
    sum_b -= sum_a
    d = (x - sum_b) // sum_a
    print(100 * d + 1)
solve()
