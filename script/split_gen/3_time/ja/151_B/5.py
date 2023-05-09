def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    if (m * n) - sum_a > k:
        print(-1)
    else:
        print((m * n) - sum_a if (m * n) - sum_a > 0 else 0)
