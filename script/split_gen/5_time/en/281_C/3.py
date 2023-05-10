def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += a[i]
    count = (t // sum) * n
    t %= sum
    for i in range(n):
        if a[i] > t:
            break
        else:
            t -= a[i]
            count += 1
    print(count + 1, t)
