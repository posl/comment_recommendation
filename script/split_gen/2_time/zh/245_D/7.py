def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    c = list(map(int,input().split()))
    b = [0 for i in range(m+1)]
    b[0] = c[0]//a[0]
    for i in range(1,m+1):
        b[i] = c[i] - sum([b[j]*a[i-j] for j in range(i)])
    print(' '.join(map(str,b)))
