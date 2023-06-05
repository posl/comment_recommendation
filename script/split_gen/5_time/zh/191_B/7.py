def main():
    n, x = map(int, input().split())
    a = [int(x) for x in input().split()]
    for i in range(n):
        if a[i] != x:
            print(a[i], end=' ')
