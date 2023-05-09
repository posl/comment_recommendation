def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    i = 0
    j = 0
    while i < N and j < M:
        if A[i] >= B[j]:
            if A[i] == B[j]:
                i += 1
            j += 1
        else:
            i += 1
    if j == M:
        print("Yes")
    else:
        print("No")
