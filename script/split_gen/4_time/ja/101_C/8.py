def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    A = A[:N - 1]
    print((N + K - 3) // (K - 1))
