def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    A.sort()
    print(sum(A[0:N-1]))
