def main():
    N, K = map(int, input().split())
    for i in range(N):
        P = list(map(int, input().split()))
        if sum(P) >= K:
            print('Yes')
        else:
            print('No')
