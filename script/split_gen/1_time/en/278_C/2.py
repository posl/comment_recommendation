def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    G = defaultdict(set)
    for _ in range(Q):
        t, a, b = map(int, input().split())
        if t == 1:
            G[a].add(b)
        elif t == 2:
            G[a].discard(b)
        else:
            print("Yes" if b in G[a] and a in G[b] else "No")
