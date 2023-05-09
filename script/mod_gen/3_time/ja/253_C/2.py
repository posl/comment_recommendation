def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    S = defaultdict(int)
    Smax = 0
    Smin = 0
    for i in range(Q):
        if query[i][0] == 1:
            S[query[i][1]] += 1
            if Smax == 0:
                Smax = query[i][1]
                Smin = query[i][1]
            else:
                if query[i][1] > Smax:
                    Smax = query[i][1]
                if query[i][1] < Smin:
                    Smin = query[i][1]
        elif query[i][0] == 2:
            if S[query[i][1]] >= query[i][2]:
                S[query[i][1]] -= query[i][2]
                if S[query[i][1]] == 0:
                    del S[query[i][1]]
            else:
                del S[query[i][1]]
                if len(S) == 0:
                    Smax = 0
                    Smin = 0
                else:
                    Smax = max(S.keys())
                    Smin = min(S.keys())
        else:
            print(Smax-Smin)

if __name__ == '__main__':
    main()