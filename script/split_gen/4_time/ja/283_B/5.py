def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    for q in query:
        if q[0] == 1:
            A[q[1] - 1] = q[2]
        else:
            print(A[q[1] - 1])
