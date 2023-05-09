def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    for i in range(n):
        if a[i] >= 3:
            p += a[i] - 2
    print(p)
