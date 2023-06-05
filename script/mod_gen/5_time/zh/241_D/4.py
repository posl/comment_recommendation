def main():
    import sys
    from bisect import bisect_left, bisect_right
    input = sys.stdin.readline
    Q = int(input())
    A = []
    for _ in range(Q):
        query = input().split()
        if query[0] == '1':
            x = int(query[1])
            A.insert(bisect_left(A, x), x)
        elif query[0] == '2':
            x, k = int(query[1]), int(query[2])
            if k > len(A) or A[-1] <= x:
                print(-1)
            else:
                print(A[bisect_left(A, x, hi=len(A)-k+1)-1])
        else:
            x, k = int(query[1]), int(query[2])
            if k > len(A) or A[0] >= x:
                print(-1)
            else:
                print(A[bisect_right(A, x, lo=k)-1])
main()
