def main():
    A = input().split()
    A = list(map(int, A))
    A.sort()
    if A[2] - A[1] == A[1] - A[0]:
        print("Yes")
    else:
        print("No")
