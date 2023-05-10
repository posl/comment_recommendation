def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [0] * N
    for i in range(N):
        B[A[i]-1] = i+1
    print(' '.join([str(i) for i in B]))
