def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(1, N):
        A[i] -= A[i-1]
    A.sort(reverse=True)
    print(A[0] + 1)
