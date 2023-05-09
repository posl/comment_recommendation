def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(N)]
    A = sorted([sorted(a) for a in A])
    A = [a[K-1:N] for a in A[K-1:N]]
    A = [a[0:N-K+1] for a in A[0:N-K+1]]
    print(min([a[0] for a in A]))
