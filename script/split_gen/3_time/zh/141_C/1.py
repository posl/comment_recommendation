def main():
    N,K,Q = map(int,input().split())
    A = [int(input()) for i in range(Q)]
    score = [K for i in range(N)]
    for i in range(Q):
        score[A[i]-1] -= 1
    for i in range(N):
        if score[i] <= 0:
            print('No')
        else:
            print('Yes')
