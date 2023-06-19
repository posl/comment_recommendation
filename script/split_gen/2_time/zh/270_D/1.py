def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    cnt = 0
    for i in range(K-1,-1,-1):
        cnt += (N//A[i])*(2**(i+1))
        N %= A[i]
    print(cnt)
