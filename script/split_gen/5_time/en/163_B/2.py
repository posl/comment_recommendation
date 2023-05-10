def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    total = sum(a)
    if total > n:
        print(-1)
    else:
        print(n - total)
