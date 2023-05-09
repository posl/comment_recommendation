def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] > K:
        print(0)
        return
    A = A[1:]
    N -= 1
    A = [A[i] - A[i - 1] - 1 for i in range(1, N)]
    A.sort()
    for i in range(N - K + 1):
        A[i] = 0
    print(sum(A) + 1)
