def main():
    import sys
    input = sys.stdin.readline
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P = [p-1 for p in P]
    #Pを累積和にする
    for i in range(N-1):
        P[i+1] += P[i]
    #print(P)
    #K番目に大きい値を求める
    for i in range(N-K+1):
        if i == 0:
            print(P[K-1])
        else:
            print(P[i+K-1] - P[i-1])
