def main():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    for i in range(n):
        if a[i] <= w:
            count += 1
            w -= a[i]
    print(count)
