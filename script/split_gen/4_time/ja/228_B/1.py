def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    for i in range(n):
        if a[i] <= x:
            count += 1
            x -= a[i]
        else:
            break
    if x > 0 and count == n:
        count -= 1
    print(count)
