def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    A_i = 0
    B_i = 0
    same = 0
    diff = 0
    while A_i < N and B_i < N:
        if A[A_i] == B[B_i]:
            same += 1
            A_i += 1
            B_i += 1
        elif A[A_i] < B[B_i]:
            A_i += 1
        else:
            B_i += 1
    A_i = 0
    B_i = 0
    while A_i < N and B_i < N:
        if A[A_i] == B[B_i]:
            A_i += 1
            B_i += 1
        elif A[A_i] < B[B_i]:
            A_i += 1
        else:
            B_i += 1
            diff += 1
    diff += N - A_i
    print(same)
    print(diff)
