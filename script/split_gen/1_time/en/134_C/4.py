def main():
    N = int(input())
    A = [int(input()) for i in range(N)]
    A.sort()
    maxA = A[-1]
    for i in range(N):
        if A[i] == maxA:
            print(A[-2])
        else:
            print(maxA)
