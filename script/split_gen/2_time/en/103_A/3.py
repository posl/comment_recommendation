def main():
    A = list(map(int, input().split()))
    A.sort()
    print(abs(A[0] - A[1]) + abs(A[1] - A[2]))
