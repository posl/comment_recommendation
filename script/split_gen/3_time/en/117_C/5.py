def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    dist = [abs(x[i + 1] - x[i]) for i in range(m - 1)]
    dist.sort()
    ans = sum(dist[:max(m - n, 0)])
    print(ans)
