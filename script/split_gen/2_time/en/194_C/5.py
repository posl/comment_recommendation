def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = 0
    for i in range(1, N):
        S += (A[i] - A[i-1])**2
    S += A[0]**2 + A[-1]**2
    for i in range(1, N-1):
        print(S - (A[i] - A[i-1])**2 - (A[i+1] - A[i])**2 + (A[i+1] - A[i-1])**2)
    print(S - A[0]**2 - A[-1]**2 + A[-1]**2 + A[0]**2)
