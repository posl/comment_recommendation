def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = [0] * n
    for i in range(n):
        b[i] = k // n
    for i in range(k % n):
        b[i] += 1
    for i in range(n):
        print(b[a.index(a[i])])
