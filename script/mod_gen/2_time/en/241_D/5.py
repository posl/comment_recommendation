def main():
    import sys
    from bisect import bisect_left, bisect_right
    input = sys.stdin.readline
    N = int(input())
    A = []
    for _ in range(N):
        q = list(map(int, input().split()))
        if q[0] == 1:
            A.append(q[1])
        elif q[0] == 2:
            k = bisect_right(A, q[1])
            if k >= q[2]:
                print(sorted(A[:k])[-q[2]])
            else:
                print(-1)
        else:
            k = bisect_left(A, q[1])
            if len(A) - k >= q[2]:
                print(sorted(A[k:])[-q[2]])
            else:
                print(-1)
    return

if __name__ == '__main__':
    main()