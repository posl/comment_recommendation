def main():
    N = int(input())
    A = list(map(int, input().split()))
    C = [0] * N
    for i in range(N):
        C[A[i]-1] += 1
    S = sum(C)
    for i in range(N):
        if C[A[i]-1] == 1:
            print(0)
        else:
            print(S - C[A[i]-1])
