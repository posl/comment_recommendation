def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    for i in range(K):
        if A[i] >= N:
            print(N)
            exit()
    ans = 0
    while N > 0:
        ans += N%A[0]
        N = N//A[0]*A[0]
        if N == 0:
            break
        while A[-1] > N:
            A.pop()
    print(ans)
