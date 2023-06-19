def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    b = [0] * n
    for i in range(k):
        b[a[i] - 1] = 1
    for i in range(q):
        for j in range(l[i] - 1, n - 1):
            if b[j] == 1 and b[j + 1] == 0:
                b[j], b[j + 1] = b[j + 1], b[j]
    for i in range(n):
        if b[i] == 1:
            print(i + 1, end=" ")
