def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = [0] * (A[-1] + 1)
    for i in range(N):
        if B[A[i]] == 0:
            for j in range(A[i], A[-1] + 1, A[i]):
                B[j] = 1
        else:
            B[A[i]] += 1
    print(N - sum(B))
