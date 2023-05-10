def main():
    n,k,q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    b = [0] * n
    for i in range(k):
        b[a[i]-1] += 1
    for i in range(q):
        b = [x-1 for x in b]
        b[l[i]-1] += 1
    for i in range(n):
        if b[i] > 0:
            print('Yes')
        else:
            print('No')
