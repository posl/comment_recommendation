def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    i = 0
    j = 0
    min = 1000000000
    while i < N and j < M:
        if abs(A[i] - B[j]) < min:
            min = abs(A[i] - B[j])
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    print(min)
