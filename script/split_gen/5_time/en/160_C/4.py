def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A = A + [K + A[0]]
    max_d = 0
    for i in range(N):
        d = A[i+1] - A[i]
        if d > max_d:
            max_d = d
    print(K - max_d)
