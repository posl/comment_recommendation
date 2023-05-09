def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[a[i] - 1] += 1
    b[x - 1] += 1
    print(b.count(1))
