def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = [int(input()) for i in range(q)]
    p = [0] * n
    for i in range(k):
        p[a[i] - 1] += 1
    for i in range(q):
        p[l[i] - 1] += 1
    for i in range(n):
        if p[i] > 0:
            print('Yes')
        else:
            print('No')
