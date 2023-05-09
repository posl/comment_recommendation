def main():
    N, K = map(int, input().split())
    C = list(map(int, input().split()))
    print(max(len(set(C[i:i+K])) for i in range(N-K+1)))
