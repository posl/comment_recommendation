def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += a[i]
    b = int(sum / n)
    c = b + 1
    sum1 = 0
    sum2 = 0
    for i in range(n):
        sum1 += abs(a[i] - b)
        sum2 += abs(a[i] - c)
    print(min(sum1, sum2))
