def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = [0]*N
    for i in range(1, N):
        A[i] = S[i-1] - A[i-1]
    for i in range(N):
        A[i] += S[-1]
    print(*A)
