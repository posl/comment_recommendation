def main():
    n,q = map(int,input().split())
    x = [int(input()) for _ in range(q)]
    a = [i+1 for i in range(n)]
    for i in range(q):
        a[x[i]-1],a[x[i]] = a[x[i]],a[x[i]-1]
    print(' '.join(map(str,a)))
