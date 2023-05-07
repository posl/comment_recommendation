def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    print(A[N-K])
