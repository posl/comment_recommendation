def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    sum = 0
    for i in range(n - 1):
        sum += a[i] * sum(a[i + 1:])
    print(sum % (10 ** 9 + 7))
