def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(N-1):
        A[i+1] = A[i] - A[i+1]
    print(A[-1])
