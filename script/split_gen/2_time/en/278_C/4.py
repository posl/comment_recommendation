def main():
    N, Q = map(int, input().split())
    F = [set() for _ in range(N)]
    for _ in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            F[A-1].add(B-1)
        elif T == 2:
            F[A-1].discard(B-1)
        else:
            if B-1 in F[A-1] and A-1 in F[B-1]:
                print("Yes")
            else:
                print("No")
    return
