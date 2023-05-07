def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    if sum(a) >= m * n:
        print(0)
    elif sum(a) + k >= m * n:
        print(m * n - sum(a))
    else:
        print(-1)
