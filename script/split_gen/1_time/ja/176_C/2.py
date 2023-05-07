def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(1, N):
        if A[i - 1] < A[i]:
            B[i] = B[i - 1] + 1
    print(sum(B))
