def main():
    n = int(input())
    a = list(map(int, input().split()))
    pos = 0
    neg = 0
    for i in range(n):
        if a[i] >= 0:
            pos += a[i]
        else:
            neg += a[i]
    print(pos - neg)
