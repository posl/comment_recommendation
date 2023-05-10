def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] != 0:
        print(0)
        return
    for i in range(1, N):
        if A[i] - A[i-1] > 1:
            print(A[i-1] + 1)
            return
    print(A[N-1] + 1)
