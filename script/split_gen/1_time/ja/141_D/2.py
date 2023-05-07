def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(M):
        A[N-1] = A[N-1] // 2
        A.sort()
    print(sum(A))
