def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    print(sum(A[:N-K]) + max(0, X * K - sum(A[:N-K])))
