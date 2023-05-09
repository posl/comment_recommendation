def main():
    N = int(input())
    S = [int(x) for x in input().split()]
    A = [0] * N
    A[0] = S[0]
    for i in range(1,N):
        A[i] = S[i] - S[i-1]
    print(*A)
