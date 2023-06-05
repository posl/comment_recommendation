def main():
    N, Q = map(int, input().split())
    users = {i: set() for i in range(1, N+1)}
    for i in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            users[A].add(B)
        elif T == 2:
            users[A].discard(B)
        else:
            print("Yes" if A in users[B] and B in users[A] else "No")
