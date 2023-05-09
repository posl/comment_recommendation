def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(0)
        return
    if N == 2:
        print(A[0] ^ A[1])
        return
    A.sort()
    if A[0] == A[1] == A[2]:
        print(0)
        return
    if A[1] == A[2]:
        print(A[0] ^ A[1])
        return
    print(A[0] ^ A[1] ^ A[2])
