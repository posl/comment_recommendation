def main():
    N, K = map(int, input().split())
    if K <= N:
        print((K-1)/N)
        return
    else:
        print(((N-K+1)/N)**2*(K-1)/N*6)
        return
