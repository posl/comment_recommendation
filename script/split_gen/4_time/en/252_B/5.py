def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [0] * n
    for i in range(k):
        c[b[i]-1] = 1
    d = []
    for i in range(n):
        if c[i] == 0:
            d.append(a[i])
    d.sort(reverse=True)
    for i in range(k):
        d.pop()
    if len(d) == 0:
        print('No')
    else:
        if max(d) > max(a):
            print('Yes')
        else:
            print('No')
