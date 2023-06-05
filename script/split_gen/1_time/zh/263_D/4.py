def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_sum(a, n, l, r))
