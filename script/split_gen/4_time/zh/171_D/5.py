def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    b = [0] * q
    c = [0] * q
    for i in range(q):
        b[i], c[i] = map(int, input().split())
    sum = 0
    for i in range(n):
        sum += a[i]
    for i in range(q):
        sum = sum - a[b[i] - 1] + c[i] * b[i]
        print(sum)
