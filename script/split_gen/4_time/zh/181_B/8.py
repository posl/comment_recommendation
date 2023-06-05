def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    sum = 0
    for i in range(n):
        sum += (a[i] + b[i]) * (b[i] - a[i] + 1) / 2
    print(int(sum))
