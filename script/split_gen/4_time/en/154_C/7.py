def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    if len(set(A)) == N:
        print('YES')
    else:
        print('NO')
