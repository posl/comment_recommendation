def main():
    N, M, T = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    battery = N
    for i in range(M):
        battery -= A[i] - B[i-1] if i > 0 else A[i]
        if battery <= 0:
            print('No')
            exit()
        battery = min(N, battery + B[i] - A[i])
    battery -= T - B[-1]
    if battery <= 0:
        print('No')
        exit()
    print('Yes')
