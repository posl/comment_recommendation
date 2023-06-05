def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    total = 0
    for i in range(n):
        if k > 0:
            total += max(a[i]-x, 0)
            k -= 1
        else:
            total += a[i]
    print(total)
