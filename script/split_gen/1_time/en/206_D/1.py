def main():
    N = int(input())
    A = list(map(int, input().split()))
    if len(A) == 1:
        print(0)
        return
    if len(A) == 2:
        if A[0] == A[1]:
            print(0)
        else:
            print(1)
        return
    if len(A) == 3:
        if A[0] == A[2]:
            print(0)
        else:
            print(1)
        return
    if len(A) == 4:
        if A[0] == A[3] and A[1] == A[2]:
            print(0)
        elif A[0] == A[3] or A[1] == A[2]:
            print(1)
        else:
            print(2)
        return
    if len(A) == 5:
        if A[0] == A[4] and A[1] == A[3]:
            print(0)
        elif A[0] == A[4] or A[1] == A[3]:
            print(1)
        else:
            print(2)
        return
    if len(A) == 6:
        if A[0] == A[5] and A[1] == A[4] and A[2] == A[3]:
            print(0)
        elif A[0] == A[5] and A[1] == A[4] or A[0] == A[5] and A[2] == A[3] or A[1] == A[4] and A[2] == A[3]:
            print(1)
        elif A[0] == A[5] or A[1] == A[4] or A[2] == A[3]:
            print(2)
        else:
            print(3)
        return
    if len(A) == 7:
        if A[0] == A[6] and A[1] == A[5] and A[2] == A[4]:
            print(0)
        elif A[0] == A[6] and A[1] == A[5] or A[0] == A[6] and A[2] == A[4] or A[1
