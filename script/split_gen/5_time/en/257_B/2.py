def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    p = [0] * n
    for i in range(q):
        p[l[i] - 1] += 1
    for i in range(n):
        if a[i] - q + sum(p) > 0:
            print('Yes')
        else:
            print('No')
