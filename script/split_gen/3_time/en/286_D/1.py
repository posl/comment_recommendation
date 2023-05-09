def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    for i in range(N):
        if A[i] <= X:
            X -= A[i]
            B[i] -= 1
    for i in range(N):
        if B[i] >= 1:
            if A[i] <= X:
                X -= A[i]
                B[i] -= 1
    if X == 0:
        print("Yes")
    else:
        print("No")
