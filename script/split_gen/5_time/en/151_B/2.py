def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    x = n*m - sum(a)
    if x > k:
        print(-1)
    elif x < 0:
        print(0)
    else:
        print(x)
