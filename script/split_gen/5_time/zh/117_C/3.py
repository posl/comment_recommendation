def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n >= m:
        print(0)
        return
    dist = [0] * (m - 1)
    for i in range(m - 1):
        dist[i] = x[i + 1] - x[i]
    dist.sort()
    print(sum(dist[:m - n]))
