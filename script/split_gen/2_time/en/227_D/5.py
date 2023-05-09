def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if K == 1:
        print(1)
        return
    if K == N:
        print(sum([x for x in A]))
        return
    if A[0] == 1:
        print(N)
        return
    for i in range(N - K + 1):
        if A[i + K - 1] - A[i] <= 1:
            print(N - K + 1)
            return
    print(N - K + 2)
    return
