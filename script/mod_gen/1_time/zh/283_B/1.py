def processQuery(q):
    if q[0] == 1:
        A[q[1]] = q[2]
    elif q[0] == 2:
        print(A[q[1]])
N = int(input())
A = [0] + list(map(int, input().split()))
Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]
for q in query:
    processQuery(q)
