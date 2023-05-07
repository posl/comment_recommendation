def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A
    A = [A[i] * A[i + 1] for i in range(N)]
    A.sort()
    print(A[K - 1])
