def main():
    # read input
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # sort A and B
    A.sort()
    B.sort()
    # find minimum difference
    i = 0
    j = 0
    min_diff = abs(A[0] - B[0])
    while i < N and j < M:
        min_diff = min(min_diff, abs(A[i] - B[j]))
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    print(min_diff)
