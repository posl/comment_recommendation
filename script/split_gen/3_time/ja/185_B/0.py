def main():
    N, M, T = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    bat = N
    for i in range(M):
        bat -= A[i] - (B[i - 1] if i > 0 else 0)
        if bat <= 0:
            print('No')
            exit()
        bat += B[i] - A[i]
        bat = min(N, bat)
    bat -= T - B[-1]
    if bat <= 0:
        print('No')
    else:
        print('Yes')
