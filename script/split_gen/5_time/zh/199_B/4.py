def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    print(len([x for x in range(1, 1001) if all([a <= x <= b for a, b in zip(A, B)])]))
