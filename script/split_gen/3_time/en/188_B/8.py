def main():
    #input
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #compute
    ab = 0
    for i in range(N):
        ab += A[i] * B[i]
    #output
    if ab == 0:
        print('Yes')
    else:
        print('No')
