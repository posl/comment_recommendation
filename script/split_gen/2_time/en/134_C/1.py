def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    m = max(a)
    for i in range(n):
        if a[i] == m:
            a[i] = 0
    m = max(a)
    for i in range(n):
        if a[i] == 0:
            a[i] = m
    for i in range(n):
        print(a[i])
