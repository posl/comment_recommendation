def main():
    from bisect import bisect_left, bisect_right
    from collections import defaultdict
    Q = int(input())
    A = []
    D = defaultdict(list)
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append(query[1])
            D[query[1]].append(_)
        elif query[0] == 2:
            i = bisect_right(A, query[1])
            if i < query[2]:
                print(-1)
            else:
                print(A[i - query[2]])
        else:
            i = bisect_left(A, query[1])
            if len(A) - i < query[2]:
                print(-1)
            else:
                print(A[i + query[2] - 1])
