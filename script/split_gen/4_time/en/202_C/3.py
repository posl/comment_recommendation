def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    #print(N, A, B, C)
    count = 0
    for i in range(N):
        count += B[C[i]-1] == A[i]
    print(count)
