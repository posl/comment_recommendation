def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    winners = [0] * N
    for i in range(Q):
        winners[L[i]-1] += 1
    for i in range(N):
        if K - Q + winners[i] > 0:
            print('Yes')
        else:
            print('No')
