def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 2:
        print(max(A))
    else:
        A.sort()
        print(max(A[0], A[-2]))
