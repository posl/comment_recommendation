def solve():
    L = int(input())
    print(2*L, L+1)
    for i in range(1, L+1):
        print(i, i+1, 0)
        print(i, i+1, 2*L-i)
solve()
