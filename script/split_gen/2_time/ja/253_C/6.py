def main():
    import sys
    from collections import Counter
    input = sys.stdin.readline
    Q = int(input())
    #S は空
    S = Counter()
    for _ in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            S[query[1]] += 1
        elif query[0] == 2:
            S[query[1]] -= min(S[query[1]],query[2])
            if S[query[1]] == 0:
                del S[query[1]]
        else:
            print(max(S.keys())-min(S.keys()))
