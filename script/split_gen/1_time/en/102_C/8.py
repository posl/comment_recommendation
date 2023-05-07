def main():
    N = int(input())
    A = list(map(int, input().split()))
    b = 0
    for i in range(N):
        b += A[i] - i - 1
    A.sort()
    b1 = b
    b2 = b
    if N % 2 == 0:
        b1 -= A[int(N/2)] - int(N/2)
        b2 -= A[int(N/2)-1] - int(N/2)
    else:
        b1 -= A[int(N/2)] - int(N/2)
        b2 -= A[int(N/2)] - int(N/2)
    print(min(abs(b1), abs(b2)))
