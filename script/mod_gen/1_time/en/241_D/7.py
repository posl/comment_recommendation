def main():
    import sys
    input = sys.stdin.readline
    import bisect
    from collections import defaultdict
    Q = int(input())
    A = []
    D = defaultdict(list)
    ans = []
    for _ in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            x = query[1]
            bisect.insort(A,x)
            D[x].append(len(A)-1)
        elif query[0] == 2:
            x,k = query[1],query[2]
            if D[x]:
                if k <= len(D[x]):
                    ans.append(A[D[x][k-1]])
                else:
                    ans.append(-1)
            else:
                if A[0] > x:
                    ans.append(-1)
                else:
                    ans.append(A[bisect.bisect_left(A,x)-k])
        elif query[0] == 3:
            x,k = query[1],query[2]
            if D[x]:
                if k <= len(D[x]):
                    ans.append(A[D[x][-k]])
                else:
                    ans.append(-1)
            else:
                if A[-1] < x:
                    ans.append(-1)
                else:
                    ans.append(A[bisect.bisect_right(A,x)+k-1])
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()