def main():
    n, k, q = map(int, input().split())
    a = [int(input()) for i in range(q)]
    p = [0] * n
    for i in range(q):
        p[a[i]-1] += 1
    for i in range(n):
        if k - (q - p[i]) > 0:
            print('Yes')
        else:
            print('No')
