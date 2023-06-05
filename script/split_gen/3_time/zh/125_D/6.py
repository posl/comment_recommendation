def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if N % 2 == 0:
        print(sum(A))
    else:
        print(sum(A[1:]) - A[0])
