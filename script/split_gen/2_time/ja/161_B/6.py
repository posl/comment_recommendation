def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    limit = total // (4 * M)
    A.sort(reverse=True)
    print("Yes" if A[M - 1] >= limit else "No")
