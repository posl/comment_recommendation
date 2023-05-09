def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    if A[0] % 2 == 0:
        print(A[0] + A[1])
    else:
        print(-1)
