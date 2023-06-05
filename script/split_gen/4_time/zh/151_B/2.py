def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    t = m * n - sum(a)
    if t > k:
        print(-1)
    elif t < 0:
        print(0)
    else:
        print(t)
