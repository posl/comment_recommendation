def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    Q1 = [0] * N
    Q2 = [0] * N
    A2 = [0] * N
    for i in range(N):
        A2[i] = A[i]
    for q in query:
        if q[0] == 1:
            Q1 = [q[1]] * N
            Q2 = [0] * N
        elif q[0] == 2:
            Q2[q[1]-1] += q[2]
        else:
            print(A2[q[1]-1] + Q1[q[1]-1] + Q2[q[1]-1])
