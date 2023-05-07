def main():
    N,K = map(int,input().split())
    p = list(map(int,input().split()))
    sum_p = 0
    for i in range(K):
        sum_p += (p[i]+1)/2
    max_p = sum_p
    for i in range(K,N):
        sum_p += (p[i]+1)/2 - (p[i-K]+1)/2
        max_p = max(max_p,sum_p)
    print(max_p)
