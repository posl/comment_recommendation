def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 2:
        print(abs(A[0] + A[1]))
        return
    if N == 3:
        print(max(abs(A[0] + A[1]), abs(A[1] + A[2]), abs(A[2] + A[0])))
        return
    if N == 4:
        print(max(abs(A[0] + A[1]), abs(A[1] + A[2]), abs(A[2] + A[3]), abs(A[3] + A[0]), abs(A[0] + A[2]), abs(A[1] + A[3])))
        return
    if N == 5:
        print(max(abs(A[0] + A[1]), abs(A[1] + A[2]), abs(A[2] + A[3]), abs(A[3] + A[4]), abs(A[4] + A[0]), abs(A[0] + A[2]), abs(A[1] + A[3]), abs(A[3] + A[1]), abs(A[2] + A[4])))
        return
    if N == 6:
        print(max(abs(A[0] + A[1]), abs(A[1] + A[2]), abs(A[2] + A[3]), abs(A[3] + A[4]), abs(A[4] + A[5]), abs(A[5] + A[0]), abs(A[0] + A[2]), abs(A[1] + A[3]), abs(A[3] + A[1]), abs(A[2] + A[4]), abs(A[4] + A[2]), abs(A[3] + A[5]), abs(A[5] + A[3]), abs(A[0] + A[4]), abs(A[4] + A[0]), abs(A[1] + A[5]), abs(A[5] + A[1])))
        return
    if N == 7:
        print(max(abs(A[0] + A[1]), abs(A[1] + A[2]), abs(A[2] + A[3]), abs(A[3] + A[4]), abs(A[4] + A
