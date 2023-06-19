def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A = sorted(A)
    B = sorted(B)
    if A[0] <= B[-1]:
        print(0)
    else:
        print(N - 1)
