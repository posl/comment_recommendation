def solve():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a for a in A if a % 2 != 0]
    if sum(A) <= X:
        print('Yes')
    else:
        print('No')
