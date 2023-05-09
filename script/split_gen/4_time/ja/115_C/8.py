def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort()
    print(h[K-1] - h[0])
