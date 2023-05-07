def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    A_max = max(A)
    A_max2 = sorted(A)[-2]
    for i in range(N):
        if A[i] == A_max:
            print(A_max2)
        else:
            print(A_max)
