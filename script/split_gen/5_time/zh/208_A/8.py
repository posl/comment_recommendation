def solve():
    A, B = map(int, input().split())
    if B <= 6 * A and B >= A:
        print('Yes')
    else:
        print('No')
