def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    sum = 0
    for i in range(N-1):
        sum += A[i] * sum(A[i+1:])
    print(sum%(10**9+7))
