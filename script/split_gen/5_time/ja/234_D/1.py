def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = []
    for i in range(N-K+1):
        ans.append(sorted(P[i:i+K])[-2])
    print(*ans, sep='\n')
