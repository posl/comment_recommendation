def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    print(max(0, min(b) - max(a) + 1))
solve()
