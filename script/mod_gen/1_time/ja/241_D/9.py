def main():
    import sys
    from bisect import bisect_left, bisect_right
    from collections import defaultdict
    input = sys.stdin.readline
    Q = int(input())
    A = []
    d = defaultdict(list)
    ans = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x = query[1]
            d[x].append(len(A))
            A.append(x)
        elif query[0] == 2:
            x = query[1]
            k = query[2]
            if k > len(d[x]):
                ans.append(-1)
            else:
                ans.append(A[d[x][k-1]])
        elif query[0] == 3:
            x = query[1]
            k = query[2]
            if k > len(A) - bisect_right(A, x):
                ans.append(-1)
            else:
                ans.append(A[bisect_right(A, x)+k-1])
    print(*ans, sep='
')
main()

if __name__ == '__main__':
    main()