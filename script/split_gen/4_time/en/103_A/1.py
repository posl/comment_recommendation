def main():
    A = [int(x) for x in input().split()]
    A.sort()
    print(A[1] - A[0] + A[2] - A[1])
