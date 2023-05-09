def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    for i in range(n):
        if a[i] + p < 4:
            p += a[i]
        else:
            p += a[i]
            p -= 4
    print(p)
