def main():
    import bisect
    import sys
    input = sys.stdin.readline
    Q = int(input())
    A = []
    ans = []
    for i in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            bisect.insort(A,query[1])
        elif query[0] == 2:
            id = bisect.bisect_right(A,query[1])
            if id < query[2]:
                ans.append(-1)
            else:
                ans.append(A[id-query[2]])
        elif query[0] == 3:
            id = bisect.bisect_left(A,query[1])
            if len(A)-id < query[2]:
                ans.append(-1)
            else:
                ans.append(A[id+query[2]-1])
    for i in ans:
        print(i)
main()

if __name__ == '__main__':
    main()