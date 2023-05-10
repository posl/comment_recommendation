def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if N % 2 == 0:
        print(B[int(N/2)] + B[int(N/2) - 1] - A[int(N/2)] - A[int(N/2) - 1] + 1)
    else:
        print(B[int(N/2)] - A[int(N/2)] + 1)
