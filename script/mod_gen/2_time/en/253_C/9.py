def main():
    from collections import defaultdict
    import sys
    readline = sys.stdin.readline
    Q = int(readline())
    S = defaultdict(int)
    minS = 10**9+1
    maxS = 0
    ans = []
    for _ in range(Q):
        query = readline().split()
        if query[0] == "1":
            x = int(query[1])
            S[x] += 1
            minS = min(minS, x)
            maxS = max(maxS, x)
        elif query[0] == "2":
            x = int(query[1])
            c = int(query[2])
            if S[x] == 0:
                continue
            if S[x] <= c:
                if x == minS:
                    minS = 10**9+1
                if x == maxS:
                    maxS = 0
            S[x] -= c
        else:
            ans.append(maxS-minS)
    print(*ans, sep="
")

if __name__ == '__main__':
    main()