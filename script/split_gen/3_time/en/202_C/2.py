def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    count = 0
    d = [0] * (n + 1)
    for i in range(n):
        d[b[c[i] - 1]] += 1
    for i in range(n):
        count += d[a[i]]
    print(count)
