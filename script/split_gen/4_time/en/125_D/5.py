def main():
    N = int(input())
    A = list(map(int, input().split()))
    m = 0
    p = 0
    for i in range(N):
        if A[i] < 0:
            m += 1
            A[i] = -A[i]
        p += A[i]
    if m % 2 == 0:
        print(p)
    else:
        print(p - 2 * min(A))
