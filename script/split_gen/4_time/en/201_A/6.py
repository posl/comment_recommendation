def main():
    A = [int(x) for x in input().split()]
    if A[0] == A[1] and A[0] == A[2]:
        print("Yes")
    elif A[0] == A[1] or A[0] == A[2] or A[1] == A[2]:
        print("No")
    else:
        A.sort()
        if A[1] - A[0] == A[2] - A[1]:
            print("Yes")
        else:
            print("No")
