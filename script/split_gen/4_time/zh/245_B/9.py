def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    m = 0
    for i in range(n):
        if a[i] > m:
            break
        m += a[i]
    print(m)
