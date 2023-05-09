def main():
    import bisect
    import sys
    Q = int(input())
    A = []
    ans = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            bisect.insort(A, query[1])
        elif query[0] == 2:
            if len(A) < query[2]:
                ans.append(-1)
            else:
                ans.append(A[-query[2]])
        elif query[0] == 3:
            if len(A) < query[2]:
                ans.append(-1)
            else:
                ans.append(A[query[2]-1])
    for i in ans:
        print(i)
    return 0
