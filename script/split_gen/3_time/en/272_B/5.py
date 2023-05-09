def main():
    N, M = map(int, input().split())
    A = [0] * N
    for _ in range(M):
        *B, = map(int, input().split())
        for i in range(1, B[0]+1):
            A[B[i]-1] += 1
    if 0 in A:
        print('No')
    else:
        print('Yes')
