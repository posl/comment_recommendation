def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    A.sort()
    B.sort()
    A_index = 0
    B_index = 0
    same_count = 0
    diff_count = 0
    while A_index < N and B_index < N:
        if A[A_index] == B[B_index]:
            same_count += 1
            A_index += 1
            B_index += 1
        elif A[A_index] < B[B_index]:
            A_index += 1
        else:
            B_index += 1
    A_index = 0
    B_index = 0
    while A_index < N and B_index < N:
        if A[A_index] == B[B_index]:
            A_index += 1
            B_index += 1
        elif A[A_index] < B[B_index]:
            A_index += 1
        else:
            B_index += 1
            diff_count += 1
    print(same_count)
    print(diff_count)
