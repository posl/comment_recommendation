def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if M == 0:
        print(1)
        exit()
    if N == M:
        print(0)
        exit()
    if N == 1:
        print(0)
        exit()
    if N == 2:
        print(1)
        exit()
    if N == 3:
        if A[0] == 1 or A[1] == 2 or A[2] == 3:
            print(1)
        else:
            print(0)
        exit()
    if N == 4:
        if A[0] == 1 or A[1] == 2 or A[2] == 3 or A[3] == 4:
            print(1)
        else:
            print(0)
        exit()
    if N == 5:
        if A[0] == 1 or A[1] == 2 or A[2] == 3 or A[3] == 4 or A[4] == 5:
            print(1)
        else:
            print(0)
        exit()
    if N == 6:
        if A[0] == 1 or A[1] == 2 or A[2] == 3 or A[3] == 4 or A[4] == 5 or A[5] == 6:
            print(1)
        else:
            print(0)
        exit()
    if N == 7:
        if A[0] == 1 or A[1] == 2 or A[2] == 3 or A[3] == 4 or A[4] == 5 or A[5] == 6 or A[6] == 7:
            print(1)
        else:
            print(0)
        exit()
    if N == 8:
        if A[0] == 1 or A[1] == 2 or A[2] == 3 or A[3] == 4 or A[4] == 5 or A[5] == 6 or A[6] == 7 or A[7] == 8:
            print(1)
        else:
            print(0)
