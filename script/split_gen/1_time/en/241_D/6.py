def main():
    import sys
    from bisect import bisect_left, bisect_right
    input = sys.stdin.readline
    Q = int(input())
    A = []
    ans = []
    for _ in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            if query[2] > len(A):
                ans.append(-1)
            else:
                ans.append(sorted(A[:bisect_right(A, query[1])])[-query[2]])
        else:
            if query[2] > len(A):
                ans.append(-1)
            else:
                ans.append(sorted(A[bisect_left(A, query[1]):])[query[2]-1])
    print(*ans, sep='
')
main()
