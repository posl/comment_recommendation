def solve():
    import sys
    from collections import defaultdict
    from heapq import heappush, heappop
    input = sys.stdin.readline
    Q = int(input())
    S = []
    cnt = defaultdict(int)
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            heappush(S, int(query[1]))
            cnt[int(query[1])] += 1
        elif query[0] == '2':
            x = int(query[1])
            c = int(query[2])
            while c > 0:
                if S[0] == x:
                    heappop(S)
                    cnt[x] -= 1
                    c -= 1
                else:
                    break
        else:
            while cnt[S[0]] == 0:
                heappop(S)
            print(S[-1] - S[0])
solve()
