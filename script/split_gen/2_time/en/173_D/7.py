def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(sum(A[0:N-1]) + A[N-1]//2)
