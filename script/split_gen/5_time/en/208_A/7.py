def solve():
    A, B = list(map(int, input().split()))
    if A <= B <= 6*A:
        print('Yes')
    else:
        print('No')
