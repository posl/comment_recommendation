def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    total = sum(A)
    limit = total / (4 * M)
    if A[M-1] >= limit:
        print("Yes")
    else:
        print("No")
