def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    B = [0] * N
    C = 0
    for q in queries:
        if q[0] == 1:
            C = q[1]
        elif q[0] == 2:
            B[q[1]-1] += q[2]
        else:
            print(A[q[1]-1] + C + B[q[1]-1])
