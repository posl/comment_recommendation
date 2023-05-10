def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    print(min(2*abs(x[i])+abs(x[i+K-1]) for i in range(N-K+1)))
