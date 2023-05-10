def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    maxA = max(A)
    for a in A:
        if a == maxA:
            print(max(A[:A.index(a)] + A[A.index(a)+1:]))
        else:
            print(maxA)
