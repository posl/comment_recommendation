def main():
    N = int(input())
    A = input().split()
    B = input().split()
    C = input().split()
    for i in range(N):
        A[i] = int(A[i])
        B[i] = int(B[i])
        C[i] = int(C[i])
    count = 0
    for i in range(N):
        count += B.count(A[C[i]-1])
    print(count)
