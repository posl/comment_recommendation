def main():
    N = int(input())
    A = [int(input()) for i in range(N)]
    maxA = max(A)
    maxAind = A.index(maxA)
    for i in range(N):
        if i == maxAind:
            print(sorted(A[:-1])[-1])
        else:
            print(maxA)
