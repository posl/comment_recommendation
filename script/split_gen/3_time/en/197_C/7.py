def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(A[0])
    else:
        print(0)
