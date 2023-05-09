def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    A.sort(reverse=True)
    A = A[:M]
    if A[M-1] >= sum_A / (4 * M):
        print("Yes")
    else:
        print("No")
