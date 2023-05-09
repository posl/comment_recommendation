def main():
    N, Q = map(int, input().split())
    # フォローしている人の集合
    follow = [set() for _ in range(N)]
    # フォローされている人の集合
    follower = [set() for _ in range(N)]
    for _ in range(Q):
        T, A, B = map(int, input().split())
        A -= 1
        B -= 1
        if T == 1:
            follow[A].add(B)
            follower[B].add(A)
        elif T == 2:
            follow[A].discard(B)
            follower[B].discard(A)
        else:
            if B in follow[A] and A in follow[B]:
                print('Yes')
            else:
                print('No')
