def solve():
    N = int(input())
    L = [int(i) for i in input().split()]
    L.sort()
    if L[N-1] < sum(L[:N-1]):
        print("是")
    else:
        print("否")
solve()
