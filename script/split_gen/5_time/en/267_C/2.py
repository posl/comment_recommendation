def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(1, N+1):
        A[i] += A[i-1]
    max_val = -10**18
    for i in range(M, N+1):
        max_val = max(max_val, A[i] - A[i-M])
    print(max_val)
