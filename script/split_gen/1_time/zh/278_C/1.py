def main():
    N, Q = map(int, input().split())
    follow = []
    for _ in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            follow.append((A, B))
        elif T == 2:
            follow.remove((A, B))
        else:
            if (A, B) in follow and (B, A) in follow:
                print("Yes")
            else:
                print("No")
