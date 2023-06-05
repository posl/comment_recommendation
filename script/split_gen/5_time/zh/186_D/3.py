def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = [0] * (n - 1)
    b[0] = a[1] - a[0]
    for i in range(1, n - 1):
        b[i] = a[i + 1] - a[i]
    print(sum(b) * 2)
