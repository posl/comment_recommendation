def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    d = {}
    for i in range(n):
        d[i+1] = 0
    for i in range(n):
        d[a[i]] += 1
    print(d)
    for i in range(n):
        print(n - d[a[i]] + 1)
