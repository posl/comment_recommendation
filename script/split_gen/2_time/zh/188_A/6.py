def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    c = []
    for i in range(n):
        c.append(a[i] + b[i])
    c.sort(reverse=True)
    sum = 0
    for i in range(n):
        if i % 2 == 0:
            sum += c[i]
        else:
            sum -= c[i]
    print(sum)
