def main():
    N, Q = map(int, input().split())
    follow = set()
    for _ in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            follow.add((A, B))
        elif T == 2:
            follow.discard((A, B))
        else:
            print('Yes' if (A, B) in follow and (B, A) in follow else 'No')
