def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # N, K = 5, 3
    # A = [6, 8, 10, 7, 10]
    # B = [2, 3, 4]
    # N, K = 5, 2
    # A = [100, 100, 100, 1, 1]
    # B = [5, 4]
    # N, K = 2, 1
    # A = [100, 1]
    # B = [2]
    A.sort()
    B.sort()
    print(A)
    print(B)
    if A[N - K] > B[0]:
        print("Yes")
    else:
        print("No")
