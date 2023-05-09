def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    Q = int(input())
    S = defaultdict(int)
    maxS = 0
    minS = 10**9
    for i in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            S[query[1]] += 1
            maxS = max(maxS,query[1])
            minS = min(minS,query[1])
        elif query[0] == 2:
            S[query[1]] -= min(query[2],S[query[1]])
            if S[query[1]] == 0:
                del S[query[1]]
                if query[1] == maxS:
                    maxS = max(S.keys()) if len(S) > 0 else 0
                if query[1] == minS:
                    minS = min(S.keys()) if len(S) > 0 else 10**9
        else:
            print(maxS - minS)
    return

if __name__ == '__main__':
    main()