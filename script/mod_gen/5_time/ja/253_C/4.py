def main():
    import sys
    from collections import Counter
    input = sys.stdin.readline
    Q = int(input())
    S = Counter()
    S_max = 0
    S_min = 0
    for _ in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            S[query[1]] += 1
            if S_max == 0:
                S_max = query[1]
                S_min = query[1]
            else:
                if S_max < query[1]:
                    S_max = query[1]
                if S_min > query[1]:
                    S_min = query[1]
        elif query[0] == 2:
            if S[query[1]] > 0:
                if S[query[1]] - query[2] > 0:
                    S[query[1]] -= query[2]
                else:
                    S[query[1]] = 0
        elif query[0] == 3:
            print(S_max - S_min)
        else:
            pass

if __name__ == '__main__':
    main()