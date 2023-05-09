def main():
    N, Q = map(int, input().split())
    following = [set() for _ in range(N)]
    for _ in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            following[A - 1].add(B - 1)
        elif T == 2:
            following[A - 1].discard(B - 1)
        else:
            if B - 1 in following[A - 1] and A - 1 in following[B - 1]:
                print("Yes")
            else:
                print("No")
