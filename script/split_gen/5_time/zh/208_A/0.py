def solve():
    A, B = map(int, input().split())
    if 6 * A < B:
        print("No")
    elif B <= A:
        print("Yes")
    else:
        print("Yes")
solve()
