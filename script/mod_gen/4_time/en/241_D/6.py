def main():
    import sys
    input = sys.stdin.readline
    from bisect import bisect_left, bisect_right
    from collections import defaultdict
    Q = int(input())
    A = []
    D = defaultdict(list)
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append(query[1])
            D[query[1]].append(i)
        elif query[0] == 2:
            x, k = query[1], query[2]
            if len(A) < k:
                print(-1)
            else:
                idx = bisect_right(A, x)
                if idx < k:
                    print(-1)
                else:
                    print(A[idx-k])
        else:
            x, k = query[1], query[2]
            if len(A) < k:
                print(-1)
            else:
                idx = bisect_left(A, x)
                if len(A)-idx < k:
                    print(-1)
                else:
                    print(A[idx+k-1])
main()
