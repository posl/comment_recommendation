def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    a.sort()
    b.sort()
    if n % 2 == 1:
        mid = n // 2
        print(b[mid] - a[mid] + 1)
    else:
        mid = n // 2
        print(b[mid] + b[mid - 1] - a[mid] - a[mid - 1] + 1)
