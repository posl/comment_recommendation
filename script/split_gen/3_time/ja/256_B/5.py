def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    for i in range(n):
        if i == 0:
            p = 0
        else:
            p += a[i-1]
    print(p)
