def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    for i in range(q):
        if l[i] == k and a[l[i]-1] < n:
            a[l[i]-1], a[l[i]] = a[l[i]], a[l[i]-1]
        elif l[i] != k and a[l[i]-1] < n and a[l[i]] > a[l[i]-1]:
            a[l[i]-1], a[l[i]] = a[l[i]], a[l[i]-1]
    for i in a:
        print(i, end=' ')
