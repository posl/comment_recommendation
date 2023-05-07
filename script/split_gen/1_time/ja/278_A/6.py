def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if k >= n:
        print(*([0] * n))
    else:
        print(*a[k:], *([0] * k))
main()
