def main():
    N = int(input())
    A = [int(input()) for i in range(N)]
    A_max = max(A)
    A_max_index = A.index(A_max)
    A_max2 = max(A[:A_max_index]+A[A_max_index+1:])
    for i in range(N):
        if i == A_max_index:
            print(A_max2)
        else:
            print(A_max)
