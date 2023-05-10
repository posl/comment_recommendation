def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] >= 0:
        print(sum(A) - 2 * A[0])
    elif A[-1] <= 0:
        print(-sum(A) + 2 * A[-1])
    else:
        print(sum(map(abs, A)))
