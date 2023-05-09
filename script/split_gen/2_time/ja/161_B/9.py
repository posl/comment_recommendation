def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    sum_A = sum(A)
    if sum_A / (4 * M) <= A[M - 1]:
        print("Yes")
    else:
        print("No")
