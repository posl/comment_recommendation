def main():
    N,K = map(int,input().split())
    h = []
    for i in range(N):
        h.append(int(input()))
    h.sort()
    min = h[K-1] - h[0]
    for i in range(1,N-K+1):
        if min > h[i+K-1] - h[i]:
            min = h[i+K-1] - h[i]
    print(min)
