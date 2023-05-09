def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    d = [0] * n
    for i in range(n):
        d[b[c[i] - 1] - 1] += 1
    print(sum([d[a[i] - 1] for i in range(n)]))
