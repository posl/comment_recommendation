def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] < 0:
        if N % 2 == 0:
            print(sum(A))
        else:
            print(sum(A) - 2 * A[0])
    else:
        print(sum(A) - 2 * A[0])
