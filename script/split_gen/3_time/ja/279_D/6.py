def solve():
    A, B = map(int, input().split())
    if A >= B:
        print(A)
    else:
        print((B-1)/2)
