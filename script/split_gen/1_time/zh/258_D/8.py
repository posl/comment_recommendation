def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    # print(N, X)
    # print(AB)
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i] = AB[i][0]
        B[i] = AB[i][1]
    # print(A)
    # print(B)
    min_time = 10 ** 20
    for i in range(N):
        time = A[i] * X + B[i] * (X - 1)
        if min_time > time:
            min_time = time
    print(min_time)
