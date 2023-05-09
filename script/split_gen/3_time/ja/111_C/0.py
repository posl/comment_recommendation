def main():
    N = int(input())
    V = list(map(int, input().split()))
    A = [V[i] for i in range(0, N, 2)]
    B = [V[i] for i in range(1, N, 2)]
    a = max(A, key=A.count)
    b = max(B, key=B.count)
    if a != b:
        print(N - max(A.count(a), B.count(b)) * 2)
    else:
        c = max(A.count(A[0]), B.count(B[0])) * 2
        d = max(A.count(A[-1]), B.count(B[-1])) * 2
        print(N - max(c, d))
