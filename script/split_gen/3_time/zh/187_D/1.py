def main():
    N = int(input())
    A, B = [], []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if N % 2 == 0:
        a = A[N//2 - 1] + A[N//2]
        b = B[N//2 - 1] + B[N//2]
        print(b-a+1)
    else:
        a = A[N//2]
        b = B[N//2]
        print(b-a+1)
