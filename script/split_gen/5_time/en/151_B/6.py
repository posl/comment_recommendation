def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    total = sum(a)
    if n*m - total > k:
        print(-1)
    elif n*m - total < 0:
        print(0)
    else:
        print(n*m - total)
