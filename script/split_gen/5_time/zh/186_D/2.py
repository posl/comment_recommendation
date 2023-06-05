def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    for i in range(n):
        count += (i * a[i] - (n - i - 1) * a[i])
    print(count * 2)
