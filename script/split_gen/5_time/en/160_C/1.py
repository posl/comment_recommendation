def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    max_distance = 0
    for i in range(n - 1):
        max_distance = max(max_distance, a[i + 1] - a[i])
    max_distance = max(max_distance, k - a[n - 1] + a[0])
    print(k - max_distance)
