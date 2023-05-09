def solve():
    N, Q = map(int, input().split())
    follow = [set() for _ in range(N)]
    for _ in range(Q):
        T, A, B = map(int, input().split())
        A -= 1
        B -= 1
        if T == 1:
            follow[A].add(B)
        elif T == 2:
            follow[B].add(A)
        else:
            if B in follow[A]:
                print("Yes")
            elif A in follow[B]:
                print("Yes")
            else:
                print("No")
solve()
import sys
input = sys.stdin.readline
