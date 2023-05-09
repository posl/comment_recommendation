def main():
    N = int(input())
    S = list(map(int,input().split()))
    A = [0] * N
    A[0] = S[0]
    for i in range(1,N):
        A[i] = A[i-1] + S[i]
    print(" ".join(map(str,A)))
