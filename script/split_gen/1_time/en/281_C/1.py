def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += a[i]
    count = (t // sum) * n
    t = t % sum
    sum = 0
    for i in range(n):
        sum += a[i]
        if sum > t:
            print(count + i + 1, sum - a[i] - t)
            break
