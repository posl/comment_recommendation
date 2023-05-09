def main():
    N, M, T = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    battery = N
    for i in range(M):
        battery -= A[i] - (B[i - 1] if i > 0 else 0)
        if battery <= 0:
            print("No")
            return
        battery += B[i] - A[i]
        if battery > N:
            battery = N
    battery -= T - B[M - 1]
    if battery <= 0:
        print("No")
    else:
        print("Yes")
