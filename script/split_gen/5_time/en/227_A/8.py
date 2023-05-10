def main():
    N, K, A = map(int, input().split())
    print((K//N + (K%N >= A))*N - (K%N < A)*(N-A))
