def main():
    N = int(input())
    A = input().split()
    A = [int(i) for i in A]
    A.sort()
    print(A[-1] - A[0])
