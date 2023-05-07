def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    for i in range(N):
        if X >= A[i]:
            X -= A[i] * B[i]
    if X == 0:
        print('Yes')
    else:
        print('No')
