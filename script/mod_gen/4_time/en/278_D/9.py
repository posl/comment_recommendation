def solve():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    #print(N, A, Q, query)
    #print(A)
    #print(query)
    for q in query:
        #print(q)
        if q[0] == 1:
            A = [q[1] for _ in range(N)]
        elif q[0] == 2:
            A[q[1]-1] += q[2]
        elif q[0] == 3:
            print(A[q[1]-1])
        else:
            print("ERROR")

if __name__ == '__main__':
    solve()