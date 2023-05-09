def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    D = [0] * N
    for i in range(N):
        D[B[C[i]-1]-1] += 1
    count = 0
    for i in range(N):
        count += D[A[i]-1]
    print(count)
