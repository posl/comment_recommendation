def main():
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    a.sort()
    b.sort()
    if n % 2 == 0:
        print(b[n//2-1] + b[n//2] - a[n//2-1] - a[n//2] + 1)
    else:
        print(b[n//2] - a[n//2] + 1)
