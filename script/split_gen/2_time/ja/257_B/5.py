def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    b = [0] * n
    for i in range(k):
        b[a[i] - 1] = i + 1
    for i in range(q):
        if b[l[i] - 1] != 0:
            if b[l[i] - 1] == k:
                b[l[i] - 1] = 0
            else:
                b[l[i] - 1] = b[l[i] - 1] + 1
    for i in range(n):
        if b[i] != 0:
            print(b[i], end=' ')
        else:
            print(0, end=' ')
