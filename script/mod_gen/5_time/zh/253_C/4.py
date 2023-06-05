def solve():
    import sys
    import bisect
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    S = []
    for i in range(Q):
        if query[i][0] == 1:
            bisect.insort(S, query[i][1])
        elif query[i][0] == 2:
            while query[i][2] > 0:
                if S.count(query[i][1]) == 0:
                    break
                S.remove(query[i][1])
                query[i][2] -= 1
        else:
            print(S[-1] - S[0])

if __name__ == '__main__':
    solve()