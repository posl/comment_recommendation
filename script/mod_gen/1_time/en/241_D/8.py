def main():
    import sys
    from bisect import bisect_left, bisect_right
    Q = int(sys.stdin.readline())
    A = []
    B = []
    C = []
    for i in range(Q):
        query = sys.stdin.readline().split()
        if query[0] == '1':
            x = int(query[1])
            A.append(x)
            B.append(x)
        elif query[0] == '2':
            x, k = int(query[1]), int(query[2])
            C.append([x, k])
        else:
            x, k = int(query[1]), int(query[2])
            C.append([x, k])
    A.sort()
    B.sort()
    for i in range(len(C)):
        if C[i][1] == 1:
            if C[i][0] < A[0]:
                print(-1)
            else:
                print(A[bisect_left(A, C[i][0]) - 1])
        elif C[i][1] == 2:
            if C[i][0] < A[0]:
                print(-1)
            else:
                print(A[bisect_left(A, C[i][0]) - 1], A[bisect_left(A, C[i][0])])
        elif C[i][1] == 3:
            if C[i][0] < A[0]:
                print(-1)
            else:
                print(A[bisect_left(A, C[i][0]) - 1], A[bisect_left(A, C[i][0])], A[bisect_left(A, C[i][0]) + 1])
        elif C[i][1] == 4:
            if C[i][0] < A[0]:
                print(-1)
            else:
                print(A[bisect_left(A, C[i][0]) - 1], A[bisect_left(A, C[i][0])], A[bisect_left(A, C[i][0]) + 1], A[bisect_left(A, C[i][0]) + 2])
        else:
            if C[i][0] < A[0]:
                print(-1)
            else:
                print(A[bisect_left(A, C[i][0]) - 1], A[bisect_left(A, C[i][0])], A[bisect_left

if __name__ == '__main__':
    main()