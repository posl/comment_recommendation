def main():
    n, q = map(int, input().split())
    x = [int(input()) for i in range(q)]
    a = [i for i in range(1, n+1)]
    for i in range(q):
        a[x[i]-1], a[x[i]] = a[x[i]], a[x[i]-1]
    print(' '.join(map(str, a)))
