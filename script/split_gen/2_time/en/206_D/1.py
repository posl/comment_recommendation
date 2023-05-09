def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(0)
        return
    if N == 2:
        if A[0] == A[1]:
            print(0)
            return
        else:
            print(1)
            return
    if N == 3:
        if A[0] == A[2]:
            print(0)
            return
        else:
            print(1)
            return
    if N == 4:
        if A[0] == A[3] and A[1] == A[2]:
            print(0)
            return
        else:
            print(1)
            return
    if N == 5:
        if A[0] == A[4] and A[1] == A[3]:
            print(0)
            return
        else:
            print(1)
            return
    if N == 6:
        if A[0] == A[5] and A[1] == A[4] and A[2] == A[3]:
            print(0)
            return
        else:
            print(1)
            return
    if N == 7:
        if A[0] == A[6] and A[1] == A[5] and A[2] == A[4]:
            print(0)
            return
        else:
            print(1)
            return
    if N == 8:
        if A[0] == A[7] and A[1] == A[6] and A[2] == A[5] and A[3] == A[4]:
            print(0)
            return
        else:
            print(1)
            return
    if N == 9:
        if A[0] == A[8] and A[1] == A[7] and A[2] == A[6] and A[3] == A[5]:
            print(0)
            return
        else:
            print(1)
            return
    if N == 10:
        if A[0] == A[9] and A[1] == A[8] and A[2] == A[7] and A[3] == A[6] and A
