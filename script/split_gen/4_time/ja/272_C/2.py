def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] % 2 == 0 or A[-1] % 2 == 0:
        print(A[-1])
    else:
        print(-1)
