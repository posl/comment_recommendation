def main():
    n, k = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    min_diff = float('inf')
    for i in range(n-k+1):
        diff = h[i+k-1] - h[i]
        min_diff = min(min_diff, diff)
    print(min_diff)
