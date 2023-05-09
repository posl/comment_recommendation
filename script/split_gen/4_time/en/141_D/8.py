def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N):
        a = A[i]
        if a <= 2 ** M:
            A[i] = 0
            M -= 1
        else:
            A[i] = a % (2 ** M)
    print(sum(A))
