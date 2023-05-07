def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    A.sort(key=lambda x: x[0])
    A.sort(key=lambda x: x[1])
    A.sort(key=lambda x: x[2])
    A.sort(key=lambda x: x[3])
    A.sort(key=lambda x: x[4])
    print(A[K - 1][K - 1])
