def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(K-1, N):
        print(sorted(P[:i+1])[-1])
    return
