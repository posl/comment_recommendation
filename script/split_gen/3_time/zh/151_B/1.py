def main():
    n, k, m = map(int, input().split())
    A = list(map(int, input().split()))
    if n * m - sum(A) > k:
        print(-1)
    else:
        print(max(0, n * m - sum(A)))
