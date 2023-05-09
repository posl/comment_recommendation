def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    if A[0]%2 == 0:
        print(A[0])
        return
    if N == 1:
        print(-1)
        return
    if A[1]%2 == 0:
        print(A[1])
        return
    print(-1)
