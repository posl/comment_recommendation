def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a = 0
    for i in range(N):
        a += A[i] * B[i]
    if a == 0:
        print('Yes')
    else:
        print('No')
