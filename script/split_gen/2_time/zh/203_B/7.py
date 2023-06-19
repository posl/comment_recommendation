def main():
    N, K = map(int, input().split())
    print((N*K*100+N*(N+1)*K//2))
