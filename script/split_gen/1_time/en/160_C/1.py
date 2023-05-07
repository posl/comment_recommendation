def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    dist = [a[i + 1] - a[i] for i in range(n - 1)]
    dist.append(k - a[-1] + a[0])
    print(k - max(dist))
