def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    # print(N)
    # print(A)
    # print(Q)
    # print(query)
    # for q in query:
    #     if q[0] == 1:
    #         for i in range(N):
    #             A[i] = q[1]
    #     elif q[0] == 2:
    #         A[q[1]-1] += q[2]
    #     else:
    #         print(A[q[1]-1])
    # for q in query:
    #     if q[0] == 1:
    #         A = [q[1] for _ in range(N)]
    #     elif q[0] == 2:
    #         A[q[1]-1] += q[2]
    #     else:
    #         print(A[q[1]-1])
    # for q in query:
    #     if q[0] == 1:
    #         A = [q[1]] * N
    #     elif q[0] == 2:
    #         A[q[1]-1] += q[2]
    #     else:
    #         print(A[q[1]-1])
    # for q in query:
    #     if q[0] == 1:
    #         A = [q[1]] * N
    #     elif q[0] == 2:
    #         A[q[1]-1] += q[2]
    #     else:
    #         print(A[q[1]-1])
    # for q in query:
    #     if q[0] == 1:
    #         A = [q[1]] * N
    #     elif q[0] == 2:
    #         A[q[1]-1] += q[2]
    #     else:
    #         print(A[q[1]-1])
    # for q in query:
    #     if q[0] == 1:
    #         A = [q[1]] * N
    #     elif q[0] == 2:
    #         A[q[1]-

if __name__ == '__main__':
    main()