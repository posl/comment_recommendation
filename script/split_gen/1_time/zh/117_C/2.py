def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n >= m:
        print(0)
        return
    dist = []
    for i in range(1, m):
        dist.append(x[i] - x[i-1])
    dist.sort()
    print(sum(dist[:m-n]))
