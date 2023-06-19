def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    q = int(input())
    b = []
    c = []
    for i in range(q):
        b_i, c_i = [int(i) for i in input().split()]
        b.append(b_i)
        c.append(c_i)
    # print(n)
    # print(a)
    # print(q)
    # print(b)
    # print(c)
    sum_a = sum(a)
    # print(sum_a)
    for i in range(q):
        sum_a = sum_a - a.count(b[i]) * b[i] + a.count(b[i]) * c[i]
        print(sum_a)
solve()
