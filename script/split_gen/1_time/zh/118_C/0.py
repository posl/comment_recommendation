def solve():
    N = int(input())
    A = list(map(int, input().split()))
    while len(A) > 1:
        A = [a % min(A) for a in A if a % min(A) > 0]
    print(min(A))
