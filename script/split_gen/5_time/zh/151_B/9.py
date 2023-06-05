def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    if n * m - sum_a <= k:
        print(max(n * m - sum_a, 0))
    else:
        print(-1)
