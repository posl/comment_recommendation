def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    A.sort()
    if N == 1:
        print(A[0])
    else:
        if A[0] == A[1]:
            print(A[-1])
        else:
            print(A[0])
