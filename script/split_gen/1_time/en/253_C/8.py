def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    #print(query)
    S = defaultdict(int)
    for q in query:
        if q[0] == 1:
            S[q[1]] += 1
        elif q[0] == 2:
            if S[q[1]] > 0:
                S[q[1]] -= min(q[2], S[q[1]])
        else:
            print(max(S.keys()) - min(S.keys()))
    return
