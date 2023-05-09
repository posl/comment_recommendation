def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = []
    for i in range(N):
        B.append(A[i] % M)
