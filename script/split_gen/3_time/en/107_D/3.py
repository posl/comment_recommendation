def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if N % 2 == 1:
        print(A[N // 2])
    else:
        print(A[N // 2 - 1])
