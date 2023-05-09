def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    b[0] = sum(a) - sum(a[1::2]) * 2
    for i in range(1, n):
        b[i] = a[i-1] * 2 - b[i-1]
    print(" ".join(map(str, b)))
