def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 2:
        print(max(A[0], A[1]))
        return
    if N == 3:
        print(max(A[0]+A[1], A[1]+A[2], A[2]+A[0]))
        return
    if N % 2 == 0:
        print(sum(A))
        return
    if N % 2 == 1:
        print(sum(A) - 2*min(A))
        return
main()
