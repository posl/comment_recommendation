def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    min_sum = sum(a[:n - l + 1])
    max_sum = sum(a[-r:])
    print(max_sum - min_sum)
