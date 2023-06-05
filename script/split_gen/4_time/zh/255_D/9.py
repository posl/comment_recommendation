def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    for i in range(Q):
        X.append(int(input()))
    sum = 0
    for i in range(N-1):
        sum += abs(A[i+1] - A[i])
    print(sum + abs(A[0] - X[0]) + abs(X[Q-1] - A[N-1]))
    for i in range(1, Q):
        if A[0] <= X[i-1] <= A[0] + A[1]:
            sum += abs(X[i-1] - A[0])
            sum += abs(X[i-1] - A[1])
            sum -= abs(A[0] - A[1])
        elif A[0] <= X[i-1] <= A[0] + A[1] + A[2]:
            sum += abs(X[i-1] - A[0])
            sum += abs(X[i-1] - A[2])
            sum -= abs(A[0] - A[1])
            sum -= abs(A[1] - A[2])
        elif A[0] <= X[i-1] <= A[0] + A[1] + A[2] + A[3]:
            sum += abs(X[i-1] - A[0])
            sum += abs(X[i-1] - A[3])
            sum -= abs(A[0] - A[1])
            sum -= abs(A[1] - A[2])
            sum -= abs(A[2] - A[3])
        elif A[0] <= X[i-1] <= A[0] + A[1] + A[2] + A[3] + A[4]:
            sum += abs(X[i-1] - A[0])
            sum += abs(X[i-1] - A[4])
            sum -= abs(A[0] - A[1])
            sum -= abs(A[1] - A[2])
            sum -= abs(A[2] - A[3])
            sum -= abs(A[3] - A[4])
        elif A[0] <= X[i-1] <= A[0] + A[1] + A[2] + A[3]
