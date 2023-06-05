def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    b = [0] * q
    c = [0] * q
    for i in range(q):
        b[i], c[i] = map(int, input().split())
    sum_a = sum(a)
    for i in range(q):
        sum_a = sum_a - a[b[i] - 1] * (b[i] - c[i]) + a[b[i] - 1] * c[i]
        print(sum_a)
