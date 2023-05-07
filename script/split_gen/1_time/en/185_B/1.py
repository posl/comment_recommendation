def main():
    N, M, T = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    now = N
    for i in range(M):
        now -= A[i] - (0 if i == 0 else B[i - 1])
        if now <= 0:
            print('No')
            return
        now += B[i] - A[i]
        now = N if now > N else now
    now -= T - B[-1]
    if now <= 0:
        print('No')
        return
    print('Yes')
