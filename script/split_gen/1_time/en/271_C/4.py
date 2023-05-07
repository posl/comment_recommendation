def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] != 1:
        print(0)
        return
    for i in range(1, N):
        if A[i] - A[i - 1] > 1:
            print(A[i - 1])
            return
    print(A[-1])
