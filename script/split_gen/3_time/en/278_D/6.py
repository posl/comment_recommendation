def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    add = [0] * N
    assigned = [None] * N
    assigned_sum = 0
    for q in query:
        if q[0] == 1:
            assigned = [q[1]] * N
            assigned_sum = q[1] * N
        elif q[0] == 2:
            if assigned[q[1] - 1]:
                assigned[q[1] - 1] += q[2]
                assigned_sum += q[2]
            else:
                add[q[1] - 1] += q[2]
        else:
            if assigned[q[1] - 1]:
                print(assigned[q[1] - 1])
            else:
                print(A[q[1] - 1] + add[q[1] - 1] + assigned_sum)
