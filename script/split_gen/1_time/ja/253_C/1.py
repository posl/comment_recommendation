def main():
    import sys
    from collections import Counter
    input = sys.stdin.readline
    Q = int(input())
    S = Counter()
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            S[query[1]] += 1
        elif query[0] == 2:
            S[query[1]] = max(S[query[1]] - query[2], 0)
        else:
            print(max(S.keys()) - min(S.keys()))
    return
