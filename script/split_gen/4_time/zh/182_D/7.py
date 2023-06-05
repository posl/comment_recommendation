def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = 0
    d = 0
    for i in range(n):
        c += a[i]
        d = max(d, c)
    print(d)
