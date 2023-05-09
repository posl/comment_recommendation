def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = list(map(int, input().split()))
        a.append(a_i)
        b.append(b_i)
    d = [0] * (n + 1)
    for i in range(n):
        d[a[i]] += 1
        d[a[i] + b[i]] -= 1
    for i in range(1, n + 1):
        d[i] += d[i - 1]
    for i in range(1, n + 1):
        print(d.count(i))
