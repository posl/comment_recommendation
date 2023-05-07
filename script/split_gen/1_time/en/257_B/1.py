def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    for i in range(q):
        a[l[i] - 1] += 1
    for i in range(k):
        if a[i] - q - 1 > 0:
            print(a[i] - q - 1, end=' ')
        else:
            print('0', end=' ')
