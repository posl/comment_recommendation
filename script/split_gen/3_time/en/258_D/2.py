def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    total = 0
    for i in range(N):
        total += A[i] + B[i]
    total -= min(B)
    print(total * (X - 1) + min(A) + min(B))
