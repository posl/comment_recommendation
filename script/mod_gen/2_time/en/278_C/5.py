def solve():
    N, Q = map(int, input().split())
    follow = [[] for _ in range(N)]
    for _ in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            follow[A-1].append(B-1)
        elif T == 2:
            if B-1 in follow[A-1]:
                follow[A-1].remove(B-1)
        else:
            if A-1 in follow[B-1] and B-1 in follow[A-1]:
                print("Yes")
            else:
                print("No")
solve()
