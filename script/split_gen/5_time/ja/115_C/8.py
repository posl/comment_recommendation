def main():
    N, K = map(int, input().split())
    h = [0] * N
    for i in range(N):
        h[i] = int(input())
    h.sort()
    min = h[K-1] - h[0]
    for i in range(N-K+1):
        if min > h[i+K-1] - h[i]:
            min = h[i+K-1] - h[i]
    print(min)
