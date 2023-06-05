def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    min_sum = 0
    for i in range(n):
        a[i] = a[i] + l
        if a[i] < l:
            a[i] = l
        elif a[i] > r:
            a[i] = r
        min_sum += a[i]
    print(min_sum)
