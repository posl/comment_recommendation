def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    # AをLで置き換える
    for i in range(N):
        if L < A[i]:
            A[i] = L
    # AをRで置き換える
    for i in range(N-1, -1, -1):
        if A[i] > R:
            A[i] = R
    print(sum(A))
