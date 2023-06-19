def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    q = int(input())
    for i in range(q):
        l, r, x = [int(i) for i in input().split()]
        print(a[l-1:r].count(x))
